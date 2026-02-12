# 📡 Calendar Subscription Guide

## What is Calendar Subscription?

Calendar subscription allows you to **subscribe to a live calendar feed** that updates automatically. Instead of downloading and importing events manually, you add a subscription URL to your calendar app once, and it stays current forever.

## ✅ Benefits

- ✅ **Auto-updates**: New events appear automatically
- ✅ **Always current**: No manual re-importing needed
- ✅ **One-time setup**: Subscribe once, updates forever
- ✅ **Syncs everywhere**: Works across all your devices
- ✅ **No duplicates**: Calendar app handles updates cleanly

## 🌐 Subscription URLs

Once you deploy this to GitHub Pages, your subscription URLs will be:

```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/heat-feed.ics
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/knicks-feed.ics
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/rangers-feed.ics
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/othersports-feed.ics
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/other-feed.ics
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/all-events-feed.ics
```

**Example:**
If your GitHub username is `johndoe` and your repo is `events-calendar`, the URL would be:
```
https://johndoe.github.io/events-calendar/heat-feed.ics
```

## 📱 How to Subscribe

### Google Calendar (Desktop)

1. Open [Google Calendar](https://calendar.google.com) on your computer
2. On the left side, find "Other calendars" and click the **+** button
3. Select **"From URL"**
4. Paste the subscription URL (e.g., `https://YOUR-USERNAME.github.io/YOUR-REPO/heat-feed.ics`)
5. Click **"Add calendar"**
6. The calendar will appear in your list!
7. **Optional:** Right-click the calendar → Settings → Choose a color

### Apple Calendar (iPhone/iPad)

1. Open **Settings** → **Calendar** → **Accounts**
2. Tap **"Add Account"** → **"Other"**
3. Tap **"Add Subscribed Calendar"**
4. Paste the subscription URL
5. Tap **"Next"** → **"Save"**
6. The calendar will sync across all your Apple devices!

### Apple Calendar (Mac)

1. Open **Calendar** app
2. Go to **File** → **New Calendar Subscription**
3. Paste the subscription URL
4. Click **"Subscribe"**
5. Choose how often to refresh (recommended: Every day)
6. Click **"OK"**

### Outlook (Web/Desktop)

1. Open [Outlook Calendar](https://outlook.office.com/calendar)
2. Click **"Add calendar"** → **"Subscribe from web"**
3. Paste the subscription URL
4. Enter a calendar name (e.g., "Miami Heat 2026")
5. Click **"Import"**
6. **Optional:** Choose a color for the calendar

### Outlook (Mobile)

1. Open Outlook app
2. Tap the calendar icon at the bottom
3. Tap the menu (three lines) → **"Add calendar"**
4. Tap **"Add Internet calendar"**
5. Paste the subscription URL
6. Tap **"Subscribe"**

## 🎨 Pro Tip: Color-Coded Categories

For the best experience, subscribe to each category as a **separate calendar** and assign colors:

1. Subscribe to `heat-feed.ics` → Color it **Red** 🔴
2. Subscribe to `knicks-feed.ics` → Color it **Yellow/Gold** 🟡
3. Subscribe to `rangers-feed.ics` → Color it **Blue** ⚪
4. Subscribe to `othersports-feed.ics` → Color it **Grey** ⚪
5. Subscribe to `other-feed.ics` → Color it **Green** 🟢

Now all Heat games appear in red, Knicks in yellow, etc!

## 🔄 Update Frequency

- **GitHub Actions**: Runs every 2 weeks to update events
- **Your Calendar App**: Checks for updates every 24 hours (varies by app)
- **Result**: New events appear within 24-48 hours

## 🆚 Subscribe vs Download

| Feature | Subscribe | Download |
|---------|-----------|----------|
| Auto-updates | ✅ Yes | ❌ No |
| One-time setup | ✅ Yes | ❌ Must re-import |
| Works offline | ⚠️ Cached | ✅ Yes |
| Best for | Long-term use | One-time access |

**Recommendation:** Use **Subscribe** for ongoing access, **Download** for sharing or offline needs.

## ❓ Troubleshooting

### Calendar not updating?

- Most calendar apps update subscribed calendars every 24 hours
- To force an update in Google Calendar: Right-click calendar → "Reload"
- To force an update in Apple Calendar: Calendar → Accounts → Select account → Refresh

### "Invalid URL" error?

- Make sure you copied the complete URL
- Ensure it starts with `https://` (not `http://`)
- Verify your GitHub Pages is enabled and working

### Events appearing twice?

- You probably downloaded AND subscribed to the same feed
- Remove the downloaded calendar, keep only the subscription

### Need to unsubscribe?

- **Google Calendar:** Right-click calendar → Settings → Remove calendar
- **Apple Calendar:** Settings → Accounts → Select account → Delete
- **Outlook:** Right-click calendar → Delete

## 📞 Support

If you encounter issues:

1. Verify GitHub Pages is deployed and accessible
2. Test the feed URL in your browser (should download an .ics file)
3. Check your calendar app's subscription settings
4. Try the "Download" option as an alternative

## 🚀 Deployment Checklist

Before sharing subscription URLs with others:

- [ ] Deploy to GitHub Pages
- [ ] Test one subscription URL in your calendar
- [ ] Verify events appear correctly
- [ ] Wait 24 hours and check if events are still there
- [ ] Share URLs with others!

## 📝 Example Message to Share

```
🏀 Subscribe to auto-updating Miami Heat games!

Just add this URL to your calendar app:
https://YOUR-USERNAME.github.io/YOUR-REPO/heat-feed.ics

Updates automatically when new games are added.
No need to re-import!
```

---

**Made with ❤️ for 2026 Events** • [View Setup Guide](README.md)
