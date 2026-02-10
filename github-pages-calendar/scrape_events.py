#!/usr/bin/env python3
"""
Event scraper for Kaseya Center and MSG venues
Runs automatically via GitHub Actions every 2 weeks
"""

import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def scrape_kaseya_events():
    """Scrape events from Kaseya Center"""
    events = []
    
    try:
        # Note: This is a placeholder - you'll need to implement actual scraping
        # based on how the Kaseya website is structured
        url = "https://www.kaseyacenter.com/calendar"
        
        # For now, we'll use the existing events as a template
        # In production, you'd scrape the actual website
        print("📍 Scraping Kaseya Center...")
        
        # TODO: Implement actual scraping logic
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # Parse events from the page...
        
    except Exception as e:
        print(f"❌ Error scraping Kaseya: {e}")
    
    return events

def scrape_msg_events():
    """Scrape events from MSG venues"""
    events = []
    
    try:
        # Note: This is a placeholder
        # MSG website uses JavaScript, so you'd need selenium or similar
        print("📍 Scraping MSG venues...")
        
        venues = [
            "Madison Square Garden",
            "Radio City Music Hall",
            "Beacon Theatre",
            "Infosys Theater at MSG"
        ]
        
        # TODO: Implement actual scraping logic for each venue
        # For MSG, you might need to use Selenium due to JavaScript
        
    except Exception as e:
        print(f"❌ Error scraping MSG: {e}")
    
    return events

def categorize_event(title, venue):
    """Categorize event by team/type"""
    title_lower = title.lower()
    
    # Dolphins - Blue
    if "dolphins" in title_lower or "miami dolphins" in title_lower:
        return "dolphins", "blue"
    
    # Knicks - Yellow
    if "knicks" in title_lower or "new york knicks" in title_lower:
        return "knicks", "yellow"
    
    # Rangers - White
    if "rangers" in title_lower or "new york rangers" in title_lower:
        return "rangers", "white"
    
    # Default - Green
    return "other", "green"

def main():
    """Main scraping function"""
    print("🚀 Starting event scraper...")
    print(f"📅 Current date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Scrape events
    kaseya_events = scrape_kaseya_events()
    msg_events = scrape_msg_events()
    
    # Combine and process
    all_events = kaseya_events + msg_events
    
    # If scraping failed or returned no events, load from existing file
    if len(all_events) == 0:
        print("⚠️  No new events scraped, keeping existing data")
        try:
            with open('events.json', 'r') as f:
                existing_data = json.load(f)
                all_events = existing_data['events']
        except:
            print("❌ Could not load existing events")
            return
    
    # Sort by date
    all_events.sort(key=lambda x: x['date'])
    
    # Create output structure
    output = {
        "lastUpdated": datetime.now().isoformat(),
        "totalEvents": len(all_events),
        "events": all_events
    }
    
    # Save to file
    with open('events.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✅ Updated events.json")
    print(f"📊 Total events: {len(all_events)}")
    print(f"🟡 Knicks: {len([e for e in all_events if e['category'] == 'knicks'])}")
    print(f"⚪ Rangers: {len([e for e in all_events if e['category'] == 'rangers'])}")
    print(f"🟢 Other: {len([e for e in all_events if e['category'] == 'other'])}")

if __name__ == "__main__":
    main()
