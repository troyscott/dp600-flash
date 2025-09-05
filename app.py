from flask import Flask, render_template, request, session, jsonify
import json
import random
import markdown
from datetime import datetime
from flashcard_loader import load_all_flashcards, reload_flashcards

app = Flask(__name__)
app.secret_key = 'dp600-study-secret-key'

# Configure markdown with common extensions
md = markdown.Markdown(extensions=[
    'extra',      # Tables, code blocks, etc.
    'codehilite', # Syntax highlighting
    'nl2br'       # Convert newlines to <br>
])

# Custom Jinja2 filter for markdown
@app.template_filter('markdown')
def markdown_filter(text):
    """Convert markdown text to HTML"""
    if not text:
        return ''
    return md.convert(str(text))

# Load flashcards from markdown files
print("🚀 Loading DP-600 flashcards from markdown files...")
FLASHCARDS = load_all_flashcards()

@app.route('/')
def index():
    # Initialize session data
    if 'score' not in session:
        session['score'] = 0
        session['streak'] = 0
        session['cards_studied'] = 0
        session['correct_answers'] = 0
    
    return render_template('index.html')

@app.route('/start-session', methods=['POST'])
def start_session():
    # Get study mode parameters
    mode = request.form.get('mode', 'all')
    topic = request.form.get('topic', '')
    time_limit = request.form.get('time', '0')
    card_count = request.form.get('count', '0')
    
    # Reset session for new study session
    session['score'] = 0
    session['streak'] = 0
    session['cards_studied'] = 0
    session['correct_answers'] = 0
    session['current_card_index'] = 0
    session['study_mode'] = mode
    session['time_limit'] = int(time_limit) if time_limit.isdigit() else 0
    session['start_time'] = datetime.now().isoformat()
    
    # Filter cards based on study mode
    cards_to_study = FLASHCARDS.copy()
    
    if mode == 'topic' and topic:
        cards_to_study = [card for card in FLASHCARDS if card['category'] == topic]
        session['topic_filter'] = topic
    elif mode == 'quick' and card_count.isdigit():
        cards_to_study = random.sample(FLASHCARDS, min(int(card_count), len(FLASHCARDS)))
    elif mode == 'timed':
        # For timed mode, we'll use all cards but track time
        session['time_remaining'] = int(time_limit) * 60  # Convert to seconds
    elif mode in ['full_study', 'flash_cards']:
        # Both modes use all cards, but different UI behavior
        cards_to_study = FLASHCARDS.copy()
    
    if not cards_to_study:
        return render_template('no_cards.html', message="No cards found for this topic.")
    
    session['shuffled_cards'] = random.sample(cards_to_study, len(cards_to_study))
    session['total_cards'] = len(cards_to_study)
    
    return get_next_card()

@app.route('/next-card')
def get_next_card():
    if 'shuffled_cards' not in session or session['current_card_index'] >= len(session['shuffled_cards']):
        # Check study mode for different completion screens
        if session.get('study_mode') in ['quick', 'full_study']:
            return render_template('quick_complete.html', 
                                 total_cards=session.get('total_cards', 0))
        else:
            return render_template('session_complete.html', 
                                 score=session.get('score', 0),
                                 total_cards=len(FLASHCARDS),
                                 correct_answers=session.get('correct_answers', 0))
    
    current_card = session['shuffled_cards'][session['current_card_index']]
    
    # For review modes (quick study, full study), just advance to next card without scoring
    if session.get('study_mode') in ['quick', 'full_study']:
        session['current_card_index'] += 1
    
    return render_template('flashcard.html', card=current_card)

@app.route('/answer', methods=['POST'])
def submit_answer():
    is_correct = request.form.get('correct') == 'true'
    
    if is_correct:
        session['score'] += 10
        session['streak'] += 1
        session['correct_answers'] += 1
    else:
        session['streak'] = 0
        session['score'] = max(0, session['score'] - 5)
    
    session['cards_studied'] += 1
    session['current_card_index'] += 1
    
    return render_template('stats.html', 
                         score=session['score'],
                         streak=session['streak'],
                         cards_studied=session['cards_studied'],
                         total_cards=len(FLASHCARDS))

@app.route('/admin/reload-flashcards')
def admin_reload_flashcards():
    """Development route to reload flashcards without restarting app"""
    global FLASHCARDS
    try:
        FLASHCARDS = reload_flashcards()
        return jsonify({
            'status': 'success',
            'message': f'Reloaded {len(FLASHCARDS)} flashcards',
            'cards_by_category': get_category_counts()
        })
    except Exception as e:
        return jsonify({
            'status': 'error', 
            'message': str(e)
        }), 500

def get_category_counts():
    """Get count of flashcards by category"""
    categories = {}
    for card in FLASHCARDS:
        category = card['category']
        categories[category] = categories.get(category, 0) + 1
    return categories

if __name__ == '__main__':
    if not FLASHCARDS:
        print("❌ No flashcards loaded! Check your content/ directory.")
        print("Expected structure:")
        print("content/")
        print("├── 01-maintain-analytics-solution/")
        print("├── 02-prepare-data/")
        print("└── 03-semantic-models/")
    else:
        print(f"✅ Ready to start! Loaded {len(FLASHCARDS)} flashcards.")
    
    app.run(debug=True)