# 🧠 Pull Request #{{PR_NUMBER}}

### 🎯 Summary
Provide a concise overview of what this PR does and why it’s needed.

---

### 🧩 What's Included
1. **Project Setup**
   - [ ] Initial configurations and base setup
2. **App Updates**
   - [ ] New apps added or existing apps updated
3. **Database / Models**
   - [ ] New models, migrations, or schema updates
4. **Infrastructure / CI**
   - [ ] Docker / CI / Deployment changes
5. **Other Changes**
   - [ ] Documentation / Code refactor / Misc updates

---

### 🧪 Testing Steps
1. [ ] Run migrations successfully
2. [ ] Confirm services run via Docker Compose
3. [ ] Verify app modules function as expected

---

### 📦 Environment
- **Branch Source:** `Dev`
- **Branch Target:** `StG`
- **DB:** PostgreSQL 16
- **Framework:** Django 5.x
- **Infra:** Docker, Docker Compose

---

### 📝 Notes
- This is **PR #1 – Initial merge from Dev → StG**
- Includes:
  - Project creation  
  - Setup for 4 main apps (`Users`, `Orders`, `Catalog`, `Inventory`)  
  - 21 database tables (based on ERD)  
  - Docker + Compose infrastructure setup  
- ✅ Verified build and migrations locally

---

### 🔖 Checklist
- [ ] Code reviewed
- [ ] Tests passed locally
- [ ] Changes verified on staging
- [ ] Documentation updated (if applicable)
