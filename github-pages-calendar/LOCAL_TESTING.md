# 🧪 Test Locally Before Deploying

Want to see how the website looks before uploading to GitHub? Follow these steps:

## Option 1: Simple Double-Click (Easiest)

1. Find `index.html` on your computer
2. Double-click it
3. It opens in your browser!
4. ✅ You can see and test everything

**Note:** Some browsers block local file:// access to JSON files. If events don't load, use Option 2.

## Option 2: Local Web Server (Recommended)

### If you have Python installed:

**On Mac/Linux:**
```bash
cd path/to/github-pages-calendar
python3 -m http.server 8000
```

**On Windows:**
```bash
cd path\to\github-pages-calendar
python -m http.server 8000
```

Then open browser to: `http://localhost:8000`

### If you have Node.js installed:

```bash
npx http-server -p 8000
```

Then open browser to: `http://localhost:8000`

### If you have VSCode:

1. Install "Live Server" extension
2. Right-click `index.html`
3. Click "Open with Live Server"

## What to Test

### ✅ Check List

- [ ] Page loads and looks good
- [ ] Events are displayed by month
- [ ] Color coding works (yellow, white, green borders)
- [ ] Filter buttons work (All, Knicks, Rangers, Other)
- [ ] Search box filters events
- [ ] Checkboxes can be selected
- [ ] "Select All" / "Deselect All" work
- [ ] Selected count updates
- [ ] "Add to Calendar" downloads ICS file
- [ ] "Download ICS File" works
- [ ] Mobile view looks good (resize browser window)
- [ ] All 114 events are present

### 🐛 Common Local Testing Issues

**Events don't load:**
- Make sure `events.json` is in the same folder as `index.html`
- Use Option 2 (local web server) instead of double-click
- Check browser console (F12) for errors

**ICS download doesn't work:**
- This is normal in local testing
- Will work fine when deployed to GitHub Pages

**Page looks broken:**
- Make sure you didn't modify `index.html` accidentally
- Try hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

## Quick Edits to Test

### Change Colors
In `index.html`, find and edit:

```css
.filter-btn.knicks.active {
    background: #FDB927;  /* Change this color */
}
```

Save, refresh browser, see changes instantly!

### Change Title
Find:
```html
<h1>🎭 2026 Events Calendar</h1>
```

Change to whatever you want!

### Add Your Name
Add after the title:
```html
<p>Curated by YOUR NAME</p>
```

## 🚀 When Ready to Deploy

Once everything looks good locally:

1. Follow steps in `QUICK_START.md`
2. Upload all files to GitHub
3. Enable GitHub Pages
4. Your site goes live!

---

**Happy testing!** 🎉
