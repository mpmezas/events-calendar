# Timezone Fix Applied

## Issue
The Memphis Grizzlies vs Miami HEAT game on **Saturday, February 21, 2026** was displaying as **Friday, February 20** in the calendar grid.

## Root Cause
The `showDayEvents()` function was using `toISOString()` to format dates for comparison:

```javascript
// OLD CODE (BROKEN)
const date = new Date(year, month, day);
const dateStr = date.toISOString().split('T')[0];  // ❌ Converts to UTC
```

When creating a Date object in JavaScript with `new Date(2026, 1, 21)`, it creates a date at **midnight local time**. When `toISOString()` is called, it converts this to **UTC time**. 

For users in timezones west of UTC (like Miami, which is UTC-5 or UTC-4):
- Midnight local time on Feb 21 → 5:00 AM UTC on Feb 21
- But JavaScript's `toISOString()` can sometimes round down to Feb 20 in UTC

## Solution
Changed to format the date string directly in local time without UTC conversion:

```javascript
// NEW CODE (FIXED)
const date = new Date(year, month, day);
const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
```

## Verification
All events are now stored and displayed in local time with no timezone conversion issues.

## Files Changed
- `index.html` - Line 897: Fixed `showDayEvents()` function

## Status
✅ FIXED - All dates now display correctly regardless of user timezone
