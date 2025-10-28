# 🤗 Hugging Face Spaces Deployment Guide

**Backend Deployment for PublicSource Classification Testing Tool**

This guide will help you deploy the backend API to Hugging Face Spaces for FREE hosting.

---

## 📋 Prerequisites

- Hugging Face account (free) - Sign up at https://huggingface.co/
- GitHub account with your testing-tool repository
- 10-15 minutes of time

---

## 🚀 Part 1: Create Hugging Face Space

### Step 1: Sign Up / Log In

1. Visit https://huggingface.co/
2. Click "Sign Up" (if new) or "Log In"
3. Complete registration if needed

### Step 2: Create New Space

1. Click your profile icon → "New Space"
2. Fill in the form:
   - **Owner:** Your username
   - **Space name:** `testable-news-classification` (or your preferred name)
   - **License:** MIT
   - **Select SDK:** Choose **"Docker"** (IMPORTANT!)
   - **Visibility:** Public (recommended) or Private
3. Click "Create Space"

You'll be taken to your new Space's page.

---

## 📤 Part 2: Upload Code to Hugging Face

### Method A: Direct Upload via Web Interface (Easiest)

1. On your Space page, click **"Files"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload these files from your testing-tool directory:
   ```
   ✅ Dockerfile
   ✅ requirements.txt
   ✅ backend/ (entire folder - drag and drop)
   ✅ archive_classifier_final.py
   ✅ enhanced_geographic_data.json
   ✅ Pittsburgh neighborhoods.xlsx
   ✅ Allegheny County Municipalities.xlsx
   ✅ .dockerignore (optional but recommended)
   ```

4. Click "Commit changes to main"

### Method B: Using Git (Advanced Users)

```bash
# Clone your Hugging Face Space
git clone https://huggingface.co/spaces/YOUR-USERNAME/testable-news-classification
cd testable-news-classification

# Copy files from testing-tool
cp -r ../path/to/testing-tool/backend ./
cp ../path/to/testing-tool/Dockerfile ./
cp ../path/to/testing-tool/requirements.txt ./
cp ../path/to/testing-tool/archive_classifier_final.py ./
cp ../path/to/testing-tool/enhanced_geographic_data.json ./
cp ../path/to/testing-tool/*.xlsx ./

# Commit and push
git add .
git commit -m "Deploy classification testing tool"
git push
```

---

## ⏳ Part 3: Wait for Build

### Step 1: Monitor Build Progress

1. Go to your Space's main page
2. You'll see "Building..." status
3. Click **"Logs"** to watch the build process

**Expected build time:** 5-15 minutes (first time only)

### Step 2: Verify Build Success

Look for these messages in the logs:
```
✓ Installing Python dependencies
✓ Downloading spaCy model
✓ Starting Flask application
✓ Running on http://0.0.0.0:7860
```

### Step 3: Check Health Endpoint

Once built, your Space will have a URL like:
```
https://YOUR-USERNAME-testable-news-classification.hf.space
```

Test the health endpoint:
```
https://YOUR-USERNAME-testable-news-classification.hf.space/api/health
```

You should see:
```json
{
  "status": "healthy",
  "service": "Classification Testing Tool",
  "version": "1.0"
}
```

---

## 🔗 Part 4: Update Frontend Configuration

Now that your backend is deployed, update the frontend to connect to it.

### Step 1: Edit frontend/index.html

Open `testing-tool/frontend/index.html` and find line ~457:

```javascript
// ⚠️ IMPORTANT: Replace YOUR-USERNAME with your Hugging Face username
const HF_BACKEND_URL = 'https://YOUR-USERNAME-testable-news-classification.hf.space';
```

Replace `YOUR-USERNAME` with your actual Hugging Face username.

**Example:**
```javascript
const HF_BACKEND_URL = 'https://ziyan0219-testable-news-classification.hf.space';
```

### Step 2: Commit and Push to GitHub

```bash
cd testing-tool
git add frontend/index.html
git commit -m "Update backend URL to Hugging Face Spaces"
git push origin main
```

---

## 🎉 Part 5: Deploy Frontend to Vercel

### Step 1: Log In to Vercel

1. Visit https://vercel.com/
2. Sign up / Log in with GitHub

### Step 2: Import Project

1. Click **"Add New..."** → **"Project"**
2. Import your GitHub repository: `TESTable-news-classification`
3. Configure:
   - **Framework Preset:** Other
   - **Root Directory:** `frontend`
   - **Build Command:** (leave empty)
   - **Output Directory:** `.` (current directory)
4. Click **"Deploy"**

### Step 3: Wait for Deployment

- Deployment takes 1-2 minutes
- You'll get a URL like: `https://testable-news-classification.vercel.app`

### Step 4: Test End-to-End

1. Visit your Vercel URL
2. You should see: `✅ Connected to backend: https://your-hf-space...`
3. Paste a test URL:
   ```
   https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
   ```
4. Click "Test"
5. Wait 3-5 seconds
6. Classification results should appear!

---

## 🔍 Troubleshooting

### Problem: Build Fails on Hugging Face

**Solution 1: Check Dockerfile**
- Ensure `Dockerfile` is in the root of your Space
- Verify it's named exactly `Dockerfile` (no extension)

**Solution 2: Check Requirements**
- Ensure `requirements.txt` is present
- Check for typos in package names

**Solution 3: Check Logs**
- Click "Logs" tab to see detailed error messages
- Look for missing dependencies or syntax errors

### Problem: Backend Returns 500 Error

**Solution: Check File Paths**
Ensure these files are in your Space:
```
✅ backend/test_api.py
✅ archive_classifier_final.py
✅ enhanced_geographic_data.json
✅ Pittsburgh neighborhoods.xlsx
✅ Allegheny County Municipalities.xlsx
```

### Problem: CORS Errors

**Solution:**
The backend already has CORS enabled in `test_api.py`:
```python
from flask_cors import CORS
CORS(app)  # Enable CORS for all routes
```

If still blocked, add to `test_api.py` line ~31:
```python
CORS(app, resources={r"/*": {"origins": "*"}})
```

### Problem: Frontend Can't Connect

**Check 1: Backend URL**
- Verify `HF_BACKEND_URL` in `frontend/index.html` is correct
- Must match your actual Hugging Face Space URL
- No trailing slash

**Check 2: Backend Running**
- Visit your HF Space URL directly
- Check if `/api/health` endpoint responds

**Check 3: Browser Console**
- Open browser DevTools (F12)
- Check Console tab for error messages
- Look for CORS or network errors

### Problem: Slow Response (10+ seconds)

**Cause:** Cold Start
- Hugging Face Spaces sleep after 2-3 hours of inactivity
- First request after sleep takes longer (loading ML models)

**Solution:**
- This is normal for free tier
- Subsequent requests will be fast (2-5 seconds)
- Consider upgrading to paid tier for always-on hosting

---

## 💰 Cost Breakdown

### Hugging Face Spaces (Backend)
- **Free Tier:** ✅ Sufficient for testing
  - 2 CPU cores
  - 16GB RAM
  - Sleeps after inactivity (cold start penalty)
  - **Cost: $0/month**

- **Upgraded Hardware:** (optional)
  - Always-on (no sleep)
  - More CPU/RAM
  - **Cost: $0.60 - $3/month**

### Vercel (Frontend)
- **Hobby Plan:** ✅ FREE
  - 100GB bandwidth/month
  - Unlimited requests
  - Custom domains
  - **Cost: $0/month**

### Total Cost: **$0/month** for free tier!

---

## 📊 Performance Expectations

### Free Tier (HF + Vercel)

**Cold Start (after sleep):**
- First request: 10-30 seconds (loading models)
- Frontend loads: 1-2 seconds

**Warm State:**
- Frontend loads: < 1 second
- Classification per article: 2-5 seconds
- Total per test: 3-7 seconds

### Upgraded Tier ($0.60/month)

**Always Warm:**
- Frontend loads: < 1 second
- Classification per article: 2-5 seconds
- No cold start delays

---

## 🔒 Security Best Practices

### 1. Keep Dependencies Updated

Regularly update `requirements.txt`:
```bash
pip list --outdated
pip install --upgrade <package-name>
```

### 2. Monitor Space Activity

Check Hugging Face Space logs regularly:
- Watch for unusual traffic patterns
- Check error rates
- Monitor resource usage

### 3. Rate Limiting (Optional)

Add to `backend/test_api.py`:
```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)
```

---

## 📈 Scaling Options

### If You Need More Performance

**Option 1: Upgrade HF Hardware**
- $0.60/month: 2 vCPU, always-on
- $3/month: 4 vCPU, 32GB RAM

**Option 2: Move to Google Cloud Run**
- Pay per request (very cheap)
- Auto-scaling
- No cold starts with min instances

**Option 3: AWS Lambda + API Gateway**
- Serverless
- Pay per execution
- Requires containerization

---

## ✅ Deployment Checklist

Before going live:

- [ ] Backend deployed to Hugging Face Spaces
- [ ] Backend health check returns 200 OK
- [ ] Frontend updated with correct HF_BACKEND_URL
- [ ] Frontend deployed to Vercel
- [ ] End-to-end test successful
- [ ] Tested with multiple articles
- [ ] Tested Excel batch upload
- [ ] Checked browser console for errors
- [ ] Documented your Space URL for team
- [ ] Shared Vercel URL with users

---

## 🎯 Success Criteria

You've successfully deployed when:

1. ✅ Hugging Face Space shows "Running" status
2. ✅ `/api/health` endpoint returns healthy status
3. ✅ Vercel deployment shows "Ready"
4. ✅ Frontend connects to backend automatically
5. ✅ Test URL classification works end-to-end
6. ✅ Excel file upload processes successfully
7. ✅ Results display correctly with all fields
8. ✅ No CORS or network errors in browser console

---

## 📞 Getting Help

### Hugging Face Support

- **Docs:** https://huggingface.co/docs/hub/spaces
- **Forum:** https://discuss.huggingface.co/
- **Discord:** https://hf.co/join/discord

### Vercel Support

- **Docs:** https://vercel.com/docs
- **Support:** https://vercel.com/support
- **Discord:** https://vercel.com/discord

### Project Issues

- **GitHub:** https://github.com/Ziyan0219/TESTable-news-classification/issues

---

## 🎉 Congratulations!

You now have a fully functional, cloud-hosted classification testing tool with:

✅ **FREE backend** on Hugging Face Spaces
✅ **FREE frontend** on Vercel
✅ **Global CDN** delivery
✅ **HTTPS** security
✅ **Auto-deployments** on git push
✅ **No server management** required

**Total Monthly Cost: $0**

Share your Vercel URL with anyone - they can now test article classifications without installing anything!

---

**Last Updated:** 2025-01-15
**Version:** 1.0
**Status:** Production Ready

**Your Deployment URLs:**
- Frontend: `https://your-project.vercel.app`
- Backend: `https://your-username-testable-news-classification.hf.space`
