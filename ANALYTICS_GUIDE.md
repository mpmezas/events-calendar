# 📊 Analytics & Subscription Tracking Guide

## Overview
This guide explains how to track engagement and subscriptions for your GitHub Pages calendar.

---

## 🎯 What Can Be Tracked

### ✅ Available Metrics:
1. **Subscribe Button Clicks** (Built-in)
   - Counts shown on the calendar page
   - Stored in browser localStorage
   - Resets if user clears browser data
   
2. **GitHub Traffic Stats** (Free)
   - Page views and unique visitors
   - Top referrers
   - Popular content
   
3. **Google Analytics** (Free, Optional)
   - Detailed visitor analytics
   - User behavior tracking
   - Real-time monitoring

### ❌ Cannot Track:
- **Active Subscriptions**: ICS feeds are static files; there's no way to know who's actively subscribed
- **Feed Refresh Requests**: When calendar apps refresh the feed (unless you use a proxy server)

---

## 📈 Method 1: Built-in Subscribe Counter (Current)

**What it does:**
- Displays total number of "Subscribe" button clicks
- Updates in real-time when users click subscribe buttons
- Stored locally in browser (per device)

**Limitations:**
- Only counts clicks, not actual subscriptions
- Different browsers/devices have separate counts
- Resets if localStorage is cleared

**How to use:**
Just use the calendar normally! The counter is already integrated.

---

## 📊 Method 2: GitHub Traffic Stats (Recommended)

**What it tracks:**
- Total page views
- Unique visitors
- Traffic sources (where visitors come from)
- Top pages
- Clone/download activity

**How to access:**
1. Go to your GitHub repository
2. Click **"Insights"** tab
3. Click **"Traffic"** in the left sidebar
4. View 14-day stats for:
   - Page views
   - Unique visitors
   - Referring sites
   - Popular content

**What you can learn:**
- How many people visit your calendar
- Which pages are most popular
- Where traffic comes from
- How often your `.ics` files are accessed

**Cost:** Free (built into GitHub)

---

## 🔍 Method 3: Google Analytics (Advanced)

**What it tracks:**
- Detailed user demographics
- User behavior and flow
- Real-time visitors
- Event tracking (subscribe clicks, downloads, etc.)
- Custom dimensions

**Setup Instructions:**

### Step 1: Create Google Analytics Account
1. Go to [analytics.google.com](https://analytics.google.com)
2. Sign in with Google account
3. Click "Start measuring"
4. Create a new property for your calendar

### Step 2: Get Tracking ID
1. After creating property, get your Measurement ID (e.g., `G-XXXXXXXXXX`)
2. Copy this ID

### Step 3: Add to Your Calendar
Add this code to `index.html` in the `<head>` section:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

### Step 4: Track Subscribe Events (Optional)
To track when users click subscribe buttons, update the `subscribeToFeed` function:

```javascript
function subscribeToFeed(category) {
    // Track with Google Analytics
    if (typeof gtag !== 'undefined') {
        gtag('event', 'subscribe_click', {
            'event_category': 'subscription',
            'event_label': category,
            'value': 1
        });
    }
    
    // Rest of the function...
    incrementSubscriptionCount();
    // ... existing code
}
```

**Cost:** Free (up to 10 million events/month)

---

## 🚀 Method 4: Third-Party Analytics (Privacy-Focused)

### Option A: Plausible Analytics
- Privacy-friendly (no cookies)
- Simple dashboard
- GDPR compliant
- **Cost:** $9/month

**Setup:**
1. Sign up at [plausible.io](https://plausible.io)
2. Add tracking script to `<head>`:
```html
<script defer data-domain="yourdomain.github.io" src="https://plausible.io/js/script.js"></script>
```

### Option B: Simple Analytics
- No cookies, privacy-first
- Beautiful dashboards
- **Cost:** $19/month

**Setup:**
1. Sign up at [simpleanalytics.com](https://simpleanalytics.com)
2. Add tracking script

---

## 🎯 Recommended Setup

**For most users:**
1. ✅ Use built-in Subscribe Counter (already included)
2. ✅ Check GitHub Traffic Stats regularly (free)
3. ⚠️ Add Google Analytics if you want detailed insights (free)

**For privacy-conscious users:**
1. ✅ Use built-in Subscribe Counter only
2. ✅ Check GitHub Traffic Stats only
3. ❌ Skip Google Analytics
4. ✅ Consider Plausible/Simple Analytics if you need more data

---

## 📌 Important Notes

### About ICS Feed Tracking:
- **Static files cannot track subscriptions** - When someone subscribes to an ICS feed, their calendar app just fetches the file periodically
- **You can track:**
  - Page visits
  - Button clicks
  - File downloads/views (via GitHub stats)
- **You cannot track:**
  - Who is actively subscribed
  - How many calendars have the feed
  - When calendar apps refresh the feed

### To Track Actual Subscriptions:
You would need to:
1. Set up a backend server
2. Proxy all ICS feed requests through the server
3. Log each request with user identification
4. This adds complexity and hosting costs

**For most use cases, the current setup is sufficient!**

---

## 📊 Example Dashboard Goals

**Basic Metrics:**
- Total page views this month: [GitHub Stats]
- Subscribe button clicks: [Built-in Counter]
- Traffic sources: [GitHub Stats]

**Advanced Metrics (with Google Analytics):**
- Average time on page
- Bounce rate
- User demographics
- Device types (mobile vs desktop)
- Most popular event categories

---

## 🔧 Need Help?

If you want to implement more advanced tracking:
1. Consider your privacy policy requirements
2. Check if you need cookie consent (GDPR/CCPA)
3. Balance tracking needs vs. user privacy
4. GitHub Traffic Stats are often sufficient for most use cases

**Remember:** The best analytics setup is the one that gives you the insights you need while respecting user privacy! 🎉
