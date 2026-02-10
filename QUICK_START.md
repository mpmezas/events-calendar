# 🚀 QUICK START GUIDE

## Get Your Calendar Website Live in 5 Minutes!

### What You're Getting

A beautiful website at `https://YOUR-USERNAME.github.io/events-calendar/` that:
- ✅ Shows all 114 events color-coded (🔵 Dolphins, 🟡 Knicks, ⚪ Rangers, 🟢 Other)
- ✅ Auto-updates every 2 weeks
- ✅ Lets visitors add events to their calendar
- ✅ Works on phone, tablet, computer
- ✅ Completely FREE (GitHub Pages)

---

## Step-by-Step Setup

### 1️⃣ Create GitHub Account (if you don't have one)
- Go to https://github.com
- Click "Sign up"
- Follow the steps (it's free!)

### 2️⃣ Create New Repository
1. Click the **+** button (top right) → "New repository"
2. **Repository name:** `events-calendar`
3. **Public** (must be public for free GitHub Pages)
4. ✅ Check "Add a README file"
5. Click **"Create repository"**

### 3️⃣ Upload Files
1. Download the `github-pages-calendar` folder from your outputs
2. In your new repository, click **"Add file"** → **"Upload files"**
3. Drag ALL files from the folder:
   - `index.html`
   - `events.json`
   - `scrape_events.py`
   - `README.md`
   - `.github/workflows/update-events.yml` (create the folders if needed)
4. Click **"Commit changes"**

### 4️⃣ Enable GitHub Pages
1. Go to **Settings** (in your repository)
2. Click **Pages** (left sidebar)
3. Under "Source": select **main** branch
4. Click **Save**
5. Wait 2 minutes ⏰

### 5️⃣ Enable Auto-Updates
1. Still in **Settings** → click **Actions** → **General**
2. Scroll to "Workflow permissions"
3. Select:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
4. Click **Save**

---

## 🎉 YOU'RE DONE!

Your website is now live at:
```
https://YOUR-USERNAME.github.io/events-calendar/
```

Replace `YOUR-USERNAME` with your actual GitHub username.

---

## 📱 Share Your Website

Copy your URL and share with:
- Friends who want to see these events
- Family members
- Social media
- Anyone interested in Knicks, Rangers, Miami events!

---

## 🔄 How Auto-Updates Work

Every 2 weeks, GitHub automatically:
1. Checks Kaseya Center website
2. Checks MSG venues websites  
3. Updates your calendar if there are new events
4. **You don't have to do anything!**

---

## 💡 Pro Tips

### Bookmark on Phone
1. Visit your website on phone
2. Add to home screen
3. Access like an app!

### Test Auto-Update Manually
1. Go to "Actions" tab in your repository
2. Click "Update Events"
3. Click "Run workflow" → "Run workflow"
4. Watch it update in real-time!

### Customize the Look
- Edit `index.html` to change colors, fonts, layout
- It's just HTML/CSS/JavaScript - customize however you want!

---

## ❓ Common Questions

**Q: Do I need to know coding?**
A: Nope! Just follow the steps above.

**Q: Does it cost money?**
A: No! GitHub Pages is 100% free for public repositories.

**Q: Can I make it private?**
A: Free GitHub Pages only works with public repos. You'd need GitHub Pro for private.

**Q: What if events are wrong?**
A: The scraper checks the actual websites. If websites update, so does your calendar!

**Q: Can I customize it?**
A: Yes! Edit any file. It's your website now!

**Q: How do I share individual events?**
A: Visitors can click "Add to Calendar" on any event to get an ICS file.

---

## 🆘 Need Help?

If something doesn't work:

1. **Check the README.md** - detailed troubleshooting there
2. **Check Actions tab** - see if workflows are running
3. **Check Settings → Pages** - make sure it's enabled
4. **Wait 2-3 minutes** - GitHub Pages takes time to deploy

---

## 🎨 What It Looks Like

Your website will have:
- 🎭 Beautiful header with gradient
- 📊 Event statistics at the top
- 🟡🟢⚪ Color-coded event cards
- 🔍 Search box to find events
- ☑️ Checkboxes to select multiple events
- 📥 Buttons to add events to calendar
- 📱 Works perfectly on mobile

---

**Enjoy your new auto-updating events calendar!** 🎉

Questions? Check the full README.md in your repository.
