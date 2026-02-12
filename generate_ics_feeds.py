#!/usr/bin/env python3
"""
Generate static ICS calendar feed files for subscription.
These files are hosted on GitHub Pages and users can subscribe to them.
"""

import json
from datetime import datetime

def create_ics_feed(events, calendar_name, category=None):
    """Create an ICS calendar feed file."""
    
    # Filter events by category if specified
    if category:
        filtered_events = [e for e in events if e.get('category') == category]
    else:
        filtered_events = events
    
    if not filtered_events:
        return None
    
    # Start ICS file
    ics = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//2026 Events Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:{calendar_name}
X-WR-TIMEZONE:America/New_York
X-WR-CALDESC:Auto-updating calendar feed for {calendar_name}
"""
    
    # Add each event
    for event in filtered_events:
        # Parse date and time
        date_parts = event['date'].split('-')
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
        
        time_parts = event['time'].split(':')
        hours, minutes = int(time_parts[0]), int(time_parts[1])
        
        # Format for ICS (YYYYMMDDTHHMMSS)
        dt_start = f"{year:04d}{month:02d}{day:02d}T{hours:02d}{minutes:02d}00"
        
        # Create unique UID
        uid = f"{event['date']}-{event['title'].replace(' ', '-')}@calendar2026"
        
        # Add event
        ics += f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}Z
DTSTART:{dt_start}
SUMMARY:{event['title']}
DESCRIPTION:{event['type']}
LOCATION:{event['venue']}
STATUS:CONFIRMED
END:VEVENT
"""
    
    ics += "END:VCALENDAR"
    return ics


def main():
    """Generate all ICS feed files."""
    
    # Load events
    with open('events.json', 'r') as f:
        data = json.load(f)
    
    events = data['events']
    
    # Define categories and their names
    categories = {
        'dolphins': 'Miami Dolphins 2026',
        'heat': 'Miami Heat 2026',
        'knicks': 'New York Knicks 2026',
        'rangers': 'New York Rangers 2026',
        'othersports': 'Other Sports 2026 (F1, Tennis, UFC)',
        'other': 'Concerts & Events 2026'
    }
    
    print("Generating ICS feed files...")
    print("=" * 60)
    
    # Generate feed for each category
    for category, name in categories.items():
        ics_content = create_ics_feed(events, name, category)
        
        if ics_content:
            filename = f"{category}-feed.ics"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(ics_content)
            
            event_count = len([e for e in events if e.get('category') == category])
            print(f"✅ Created {filename} ({event_count} events)")
        else:
            print(f"⚠️  Skipped {category} (no events)")
    
    # Generate "All Events" feed
    all_ics = create_ics_feed(events, "All 2026 Events")
    with open('all-events-feed.ics', 'w', encoding='utf-8') as f:
        f.write(all_ics)
    print(f"✅ Created all-events-feed.ics ({len(events)} events)")
    
    print("=" * 60)
    print("ICS feed files generated successfully!")
    print("\nThese files can now be subscribed to via:")
    print("  https://YOUR-USERNAME.github.io/YOUR-REPO/FILENAME.ics")


if __name__ == '__main__':
    main()
