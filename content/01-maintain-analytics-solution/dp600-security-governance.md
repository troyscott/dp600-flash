# Security and Governance - DP-600 Flashcards

## Workspace-Level Access Controls

### Card 1
**Q:** What are the four main workspace roles in Microsoft Fabric?
**A:** 
- **Admin** - Full control including workspace management
- **Member** - Can create/edit content, manage datasets
- **Contributor** - Can create/edit content, limited dataset management  
- **Viewer** - Read-only access to workspace content

**Difficulty:** Basic
**Tags:** workspace, roles, permissions

---

### Card 2
**Q:** What permissions does a Workspace Member have that a Contributor doesn't?
**A:** 
- Publish apps from the workspace
- Update app metadata and permissions
- Schedule data refresh for datasets they don't own
- Delete workspace items

**Difficulty:** Intermediate
**Tags:** workspace, member, contributor, permissions

---

### Card 3
**Q:** How do you implement row-level security (RLS) in Fabric?
**A:** 
1. Create roles in the semantic model using DAX filters
2. Define DAX expressions like: `[Territory] = USERNAME()`
3. Assign users/groups to roles in workspace settings
4. Test using "View as Role" feature

**Difficulty:** Advanced
**Tags:** rls, security, dax, semantic-model

---

## Item-Level Access Controls

### Card 4
**Q:** What's the difference between item permissions and workspace roles?
**A:** 
- **Workspace roles** apply to all items in the workspace
- **Item permissions** are granular, set per individual item (dataset, report, etc.)
- Item permissions can override workspace permissions (more restrictive)

**Difficulty:** Intermediate
**Tags:** item-permissions, workspace-roles

---

### Card 5
**Q:** Which Fabric items support direct sharing?
**A:** 
- Reports
- Dashboards  
- Apps
- Semantic models
- Dataflows
- Notebooks (read-only)

**Difficulty:** Basic
**Tags:** sharing, items, fabric

---

## Sensitivity Labels

### Card 6
**Q:** What happens when you apply a sensitivity label to a dataset?
**A:** 
- Label propagates to downstream items (reports, dashboards)
- Encryption may be applied based on label settings
- Access policies defined in Microsoft Purview are enforced
- Export restrictions may apply

**Difficulty:** Advanced
**Tags:** sensitivity-labels, purview, encryption

---

### Card 7
**Q:** Can you change a sensitivity label to a less restrictive one?
**A:** 
Only if you have **Change** permissions for that label type in Microsoft Purview. Otherwise, you can only apply more restrictive labels or remove labels (if permitted).

**Difficulty:** Intermediate
**Tags:** sensitivity-labels, permissions

---

## Endorsement

### Card 8
**Q:** What are the three endorsement levels in Fabric?
**A:** 
1. **None** - Default state
2. **Promoted** - Workspace members can promote items
3. **Certified** - Only designated certifiers can certify items

**Difficulty:** Basic
**Tags:** endorsement, promoted, certified

---

### Card 9
**Q:** What's required to certify a semantic model?
**A:** 
- Must be a designated **certifier** (set by Fabric admin)
- Model must meet organization's certification criteria
- Certification can include description explaining why it's certified
- Only one certification level per item

**Difficulty:** Intermediate
**Tags:** certification, semantic-model, admin

---

## OneLake Security

### Card 10
**Q:** How does OneLake handle file-level security?
**A:** 
- Inherits Access Control Lists (ACLs) from source systems
- Supports POSIX-style permissions  
- Can use Azure AD security groups
- Integrates with Fabric workspace security model

**Difficulty:** Advanced
**Tags:** onelake, acl, file-security

---

### Practice Scenario

**Q:** You have a workspace with financial data. The CFO needs full access, analysts need read access to reports but not underlying data, and external auditors need read-only access to specific reports only. How do you configure this?

**A:** 
1. **CFO** - Workspace Admin role
2. **Analysts** - Workspace Viewer role + direct report sharing permissions  
3. **External auditors** - No workspace access + specific report sharing with view-only permissions
4. **Additional:** Apply appropriate sensitivity labels and consider RLS for data segregation

**Difficulty:** Expert
**Tags:** scenario, mixed-permissions, real-world