# GitHub Repository Setup Guide

## 🎯 Goal

Set up the TESTable-news-classification repository at:
`https://github.com/Ziyan0219/TESTable-news-classification`

---

## 📋 Pre-Setup Checklist

- [ ] Ensure all files are in `testing-tool/` directory
- [ ] Review README.md for accuracy
- [ ] Test frontend locally
- [ ] Test backend locally
- [ ] Check all links in documentation

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Create GitHub Repository

1. Go to https://github.com/Ziyan0219
2. Click "New repository"
3. Settings:
   - Repository name: `TESTable-news-classification`
   - Description: `Standalone testing platform for PublicSource article geographic classification with NLP-powered analysis`
   - Visibility: **Public** (for Vercel deployment)
   - ✅ Initialize with README (uncheck - we have our own)
   - ✅ Add .gitignore (uncheck - we have our own)
   - License: MIT (or select MIT License from dropdown)
4. Click "Create repository"

### Step 2: Initialize Local Repository

```bash
# Navigate to testing-tool directory
cd C:\Users\32044\Desktop\agents\publicsource-integrated-dashboard\testing-tool

# Initialize git
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: PublicSource classification testing tool"

# Add remote
git remote add origin https://github.com/Ziyan0219/TESTable-news-classification.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify Upload

Go to https://github.com/Ziyan0219/TESTable-news-classification

You should see:
- ✅ README.md as homepage
- ✅ frontend/ directory
- ✅ backend/ directory
- ✅ All documentation files
- ✅ LICENSE file
- ✅ .gitignore

---

## 📝 Repository Settings

### Topics (Add in GitHub)

Click "⚙️ Settings" → "Add topics":
- `classification`
- `nlp`
- `geographic-classification`
- `news-classification`
- `spacy`
- `machine-learning`
- `flask`
- `vercel`
- `testing-tool`
- `publicsource`

### About Section

**Description:**
```
Standalone testing platform for PublicSource article geographic classification with NLP-powered analysis
```

**Website:**
```
https://testable-news-classification.vercel.app
```

---

## 🌐 Deploy to Vercel

### Option 1: Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Select "Import Git Repository"
4. Choose `Ziyan0219/TESTable-news-classification`
5. Configure:
   - **Framework Preset:** Other
   - **Root Directory:** `./`
   - **Build Command:** (leave empty)
   - **Output Directory:** `frontend`
   - **Install Command:** (leave empty)
6. Click "Deploy"
7. Wait 2-3 minutes
8. Get URL: `https://testable-news-classification.vercel.app`

### Option 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to repo
cd C:\Users\32044\Desktop\agents\publicsource-integrated-dashboard\testing-tool

# Login to Vercel
vercel login

# Deploy
vercel

# Follow prompts:
# Set up and deploy? Y
# Which scope? (select your account)
# Link to existing project? N
# Project name? TESTable-news-classification
# Directory? ./
# Override settings? N

# Production deployment
vercel --prod
```

### Step 4: Configure Domain (Optional)

If you have a custom domain:
1. Go to Vercel dashboard → Your project
2. Click "Settings" → "Domains"
3. Add custom domain: `classification.yourdomain.com`
4. Follow DNS setup instructions

---

## 📊 Repository Structure

After setup, your repo should look like:

```
TESTable-news-classification/
├── frontend/
│   └── index.html                 # Frontend application
├── backend/
│   └── test_api.py                # Backend API server
├── README.md                      # Main documentation
├── DEPLOYMENT.md                  # Deployment guide
├── VERCEL_ANALYSIS.md             # Vercel compatibility analysis
├── GITHUB_SETUP.md                # This file
├── QUICK_START.md                 # Quick start guide
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
└── vercel.json                    # Vercel configuration
```

---

## 🔗 Update Links

After deployment, update placeholders in README.md:

```bash
# Replace in README.md:
# Line 3: Demo link
[![Demo](https://img.shields.io/badge/Demo-Live-brightgreen)](https://testable-news-classification.vercel.app)

# Line 43: Live demo link
Visit the live demo: **[TESTable Classification Tool](https://testable-news-classification.vercel.app)**
```

---

## 📱 Configure Backend URL in Frontend

After deploying backend to cloud, update `frontend/index.html`:

```javascript
// Line 449 - change from localhost to your backend URL
const API_URL = 'https://your-backend.example.com/api/test-classify';
```

Then commit and push:
```bash
git add frontend/index.html
git commit -m "Update backend API URL to production"
git push origin main
```

Vercel will auto-deploy the update!

---

## 🎨 GitHub Repository Enhancements

### Add Repository Description

In GitHub repository page:
1. Click "⚙️" next to About
2. Add description: "Standalone testing platform for PublicSource article geographic classification with NLP-powered analysis"
3. Add website: `https://testable-news-classification.vercel.app`
4. Add topics (see above)
5. ✅ Save

### Create Release

1. Go to "Releases" tab
2. Click "Create a new release"
3. Tag version: `v2.0`
4. Release title: "v2.0 - Production Release"
5. Description:
   ```markdown
   ## 🎉 Production Release v2.0

   ### Features
   - ✅ Single URL and Excel batch testing
   - ✅ Advanced NLP-based geographic classification
   - ✅ Real-time formatted results
   - ✅ Vercel-ready frontend
   - ✅ Full API documentation

   ### Deployment
   - Frontend: Deploy to Vercel (1-click)
   - Backend: Deploy to AWS/GCP/Heroku (see DEPLOYMENT.md)

   ### Documentation
   - [README.md](README.md) - Complete guide
   - [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment instructions
   - [VERCEL_ANALYSIS.md](VERCEL_ANALYSIS.md) - Vercel compatibility
   ```
6. Publish release

### Add Badges (Optional)

Add to top of README.md:
```markdown
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-brightgreen)](https://testable-news-classification.vercel.app)
[![Backend](https://img.shields.io/badge/Backend-Python%203.11+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Classification](https://img.shields.io/badge/Accuracy-95%25+-success)](README.md#classification-results)
```

---

## ✅ Verification Checklist

After setup, verify:

### GitHub Repository
- [ ] Repository is public
- [ ] All files uploaded
- [ ] README displays correctly
- [ ] LICENSE file present
- [ ] Topics added
- [ ] Description set

### Vercel Deployment
- [ ] Deployment successful
- [ ] Frontend loads at Vercel URL
- [ ] UI works correctly
- [ ] Links are functional
- [ ] Mobile responsive

### Functionality
- [ ] Can enter URL in input
- [ ] Can upload Excel file
- [ ] Results display correctly
- [ ] Copy/Clear buttons work
- [ ] Error messages show
- [ ] Info section expands

### Documentation
- [ ] README links work
- [ ] DEPLOYMENT.md is accurate
- [ ] VERCEL_ANALYSIS.md is complete
- [ ] All placeholders replaced

---

## 🔄 Continuous Deployment

Vercel automatically deploys on every push:

```bash
# Make changes
git add .
git commit -m "Update: description of changes"
git push origin main

# Vercel detects push and redeploys (1-2 minutes)
```

### Branch Protection (Recommended)

1. Go to Settings → Branches
2. Add rule for `main` branch
3. Enable:
   - ✅ Require pull request before merging
   - ✅ Require status checks to pass
4. Save

---

## 📞 Support

If you encounter issues:

### GitHub Issues
- Create issues at: `https://github.com/Ziyan0219/TESTable-news-classification/issues`
- Template:
  ```
  **Issue:** Brief description
  **Steps to Reproduce:** 1. ... 2. ... 3. ...
  **Expected:** What should happen
  **Actual:** What actually happens
  **Screenshots:** If applicable
  ```

### Common Problems

**Problem:** Push rejected
```bash
# Solution: Pull first
git pull origin main --rebase
git push origin main
```

**Problem:** Large files rejected
```bash
# Solution: Check .gitignore includes large files
# Do not commit:
# - *.csv, *.xlsx (test data)
# - __pycache__/
# - /tmp/
```

**Problem:** Vercel build failed
```bash
# Solution: Check vercel.json configuration
# Ensure output directory is correct: "frontend"
```

---

## 🎯 Next Steps

After successful setup:

1. **Test the deployment:**
   - Visit Vercel URL
   - Test with sample article
   - Verify all features work

2. **Deploy backend:**
   - Choose cloud provider (AWS/GCP/Heroku)
   - Follow [DEPLOYMENT.md](DEPLOYMENT.md)
   - Update API_URL in frontend

3. **Share with team:**
   - Send Vercel URL
   - Provide backend setup instructions
   - Gather feedback

4. **Monitor usage:**
   - Check Vercel analytics
   - Review backend logs
   - Track classification accuracy

---

**Setup Time:** ~10 minutes
**Status:** Ready for Production
**Last Updated:** 2025-01-15
