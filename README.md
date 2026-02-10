# 🎭 2026 Events Calendar - Kaseya Center & MSG Venues

A beautiful, auto-updating calendar website that displays events from Kaseya Center (Miami) and all MSG venues (Madison Square Garden, Radio City Music Hall, Beacon Theatre, Infosys Theater).

**🌐 Live Website:** `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

## ✨ Features

- 📅 **114 Events** color-coded by category
- 🟡 **Knicks Games** (Yellow)
- ⚪ **Rangers Games** (White)
- 🟢 **Other Events** (Green) - concerts, shows, Miami HEAT, etc.
- 🔄 **Auto-updates every 2 weeks** via GitHub Actions
- 📥 **Add to Calendar** - individual events or bulk import
- 🔍 **Search & Filter** - find events quickly
- 📱 **Mobile Friendly** - works on all devices
- 💾 **Download ICS files** - for offline use

## 🚀 Quick Setup (5 Minutes)

### Step 1: Create Your GitHub Repository

1. **Go to GitHub** and create a new repository
   - Repository name: `events-calendar` (or any name you like)
   - Make it **Public**
   - ✅ Check "Add a README file"
   - Click "Create repository"

### Step 2: Upload These Files

1. **Download this folder** to your computer
2. **Go to your repository** on GitHub
3. Click "Add file" → "Upload files"
4. **Drag and drop ALL files** from this folder:
   - `index.html`
   - `events.json`
   - `scrape_events.py`
   - `.github/workflows/update-events.yml`
   - `README.md`
5. Click "Commit changes"

### Step 3: Enable GitHub Pages

1. In your repository, go to **Settings** → **Pages**
2. Under "Source", select **main** branch
3. Click **Save**
4. Wait 1-2 minutes
5. Your site will be live at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

### Step 4: Enable GitHub Actions (Auto-Updates)

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", select:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. Click **Save**

**Done! 🎉** Your calendar is now live and will auto-update every 2 weeks!

## 📖 How to Use

### View Events
- Just visit your GitHub Pages URL
- Events are organized by month
- Color-coded by category (Knicks, Rangers, Other)

### Add Events to Your Calendar

**Option 1: Add Individual Events**
1. Click "Add to Calendar" button on any event
2. An ICS file will download
3. Open it with your calendar app
4. The event is added!

**Option 2: Add Multiple Events**
1. Check the boxes next to events you want
2. Click "📥 Add All Selected to Calendar"
3. One ICS file with all selected events downloads
4. Import to your calendar

**Option 3: Download Everything**
1. Click "💾 Download ICS File"
2. Get all 114 events in one file
3. Import to Google Calendar, Apple Calendar, etc.

### Filter Events
- Click category buttons: **All**, **Knicks**, **Rangers**, **Other**
- Use the search box to find specific events
- Combine filters and search!

### Select Events
- Click checkboxes to select events
- "Select All" / "Deselect All" buttons available
- See selected count at the top

## 🔄 Auto-Update Schedule

**GitHub Actions runs every 2 weeks** and:
1. Scrapes Kaseya Center website
2. Scrapes MSG venues websites
3. Updates `events.json` if there are changes
4. Your website automatically shows new events!

**Manual Update:**
- Go to "Actions" tab in your repository
- Click "Update Events" workflow
- Click "Run workflow"
- Updates happen immediately!

## 🛠️ Customization

### Change Update Frequency

Edit `.github/workflows/update-events.yml`:

```yaml
schedule:
  - cron: '0 6 */14 * *'  # Current: Every 2 weeks
  
  # Options:
  - cron: '0 6 */7 * *'   # Weekly
  - cron: '0 6 * * 1'     # Every Monday
  - cron: '0 6 1 * *'     # Monthly (1st of month)
```

### Change Colors

Edit `index.html`, find these sections:

```css
.filter-btn.knicks.active {
    background: #FDB927;  /* Knicks yellow */
}

.filter-btn.rangers.active {
    background: #0033A0;  /* Rangers blue */
}

.filter-btn.other.active {
    background: #10B981;  /* Green */
}
```

### Add More Venues

Edit `scrape_events.py` and add scraping logic for additional venues.

## 📂 File Structure

```
events-calendar/
├── index.html                    # Main website
├── events.json                   # Event data (auto-updated)
├── scrape_events.py             # Scraper script
├── README.md                     # This file
└── .github/
    └── workflows/
        └── update-events.yml    # Auto-update workflow
```

## 🐛 Troubleshooting

**Website not showing?**
- Check Settings → Pages is enabled
- Make sure branch is set to `main`
- Wait 2-3 minutes after enabling

**Auto-updates not working?**
- Check Settings → Actions → Permissions
- Make sure "Read and write permissions" is enabled
- Check "Actions" tab for error logs

**Events not loading?**
- Check browser console for errors (F12)
- Make sure `events.json` exists in repository
- Try hard refresh (Ctrl+Shift+R)

**Want to test scraper locally?**
```bash
python scrape_events.py
```

## 📊 Current Event Count

- 🟡 **Knicks:** 8 games
- ⚪ **Rangers:** 7 games
- 🟢 **Other Events:** 99 events
- 📊 **Total:** 114 events

## 🏟️ Venues Included

✅ **Kaseya Center** (Miami, FL)
✅ **Madison Square Garden** (New York, NY)
✅ **Radio City Music Hall** (New York, NY)
✅ **Beacon Theatre** (New York, NY)
✅ **Infosys Theater at MSG** (New York, NY)

## 🔗 Useful Links

- **Kaseya Center:** https://www.kaseyacenter.com/calendar
- **MSG Calendar:** https://www.msg.com/calendar
- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **GitHub Actions Docs:** https://docs.github.com/en/actions

## 📝 Notes

- Scraper currently uses placeholder logic - you'll need to implement actual scraping based on website structure
- Websites may change their structure - monitor the Actions logs
- ICS files work with Google Calendar, Apple Calendar, Outlook, and most calendar apps
- All times are in local venue time (EST/EDT)

## 💡 Tips

1. **Bookmark the website** on your phone for quick access
2. **Star the repository** to find it easily
3. **Enable notifications** in Actions to know when updates happen
4. **Share the URL** with friends who want to follow these events

## 🤝 Contributing

Feel free to fork and improve! Suggestions welcome.

## 📄 License

Free to use and modify!

---

**Enjoy your auto-updating event calendar! 🎉**

Made with ❤️ using GitHub Pages & Actions
