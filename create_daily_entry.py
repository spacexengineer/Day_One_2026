#!/usr/bin/env python3
"""
Daily Entry Creator for Day_One_2026 Challenge

This script helps create a new daily entry file based on the current date.
Usage: python create_daily_entry.py [optional_date_YYYY-MM-DD]
"""

import os
import sys
from datetime import datetime, timedelta


def get_day_of_year(date):
    """Calculate which day of the year it is."""
    return (date - datetime(date.year, 1, 1)).days + 1


def create_daily_entry(target_date=None):
    """Create a new daily entry file for the specified or current date."""
    
    # Use target date or today's date
    if target_date:
        try:
            date = datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD")
            return False
    else:
        date = datetime.now()
    
    # Validate year
    if date.year != 2026:
        print("❌ This challenge is for 2026 only!")
        return False
    
    # Calculate day of year
    day_num = get_day_of_year(date)
    
    # Format paths
    month_name = date.strftime("%B")
    month_num = date.strftime("%m")
    day_file = f"day{date.day:02d}.md"
    month_dir = f"2026/{month_num}_{month_name}"
    file_path = os.path.join(month_dir, day_file)
    
    # Check if file already exists
    if os.path.exists(file_path):
        print(f"⚠️  Entry already exists: {file_path}")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != 'y':
            print("✅ Keeping existing entry.")
            return True
    
    # Create directory if it doesn't exist
    os.makedirs(month_dir, exist_ok=True)
    
    # Calculate total days in the year
    total_days = (datetime(date.year, 12, 31) - datetime(date.year, 1, 1)).days + 1
    
    # Create the daily entry content
    content = f"""# Day {day_num} - {date.strftime('%B %d, %Y')}

## 🎯 Daily Goal
[What do you want to accomplish today?]

## 📝 What I Learned Today
- [Key takeaway 1]
- [Key takeaway 2]
- [Key takeaway 3]

## 💻 Code Written
[Brief description of what you coded today]

```python
# Optional: Include a code snippet
```

## 🔗 Resources
- [Link to tutorials, articles, or documentation]

## 📊 Progress
- Day {day_num} of {total_days} complete ✅

## 💭 Reflections
[Your thoughts about today's coding session, challenges faced, victories achieved]

---

**Time Spent**: [X hours]  
**Focus Areas**: [Topics or technologies you worked with]
"""
    
    # Write the file
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created daily entry: {file_path}")
    print(f"📅 Day {day_num} of {total_days} ({date.strftime('%B %d, %Y')})")
    print(f"🎯 Don't forget to fill it out and commit your progress!")
    
    return True


def main():
    """Main entry point for the script."""
    print("🚀 Day One 2026 - Daily Entry Creator")
    print("=" * 50)
    
    # Check if date argument is provided
    target_date = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Create the entry
    success = create_daily_entry(target_date)
    
    if success:
        print("\n💪 Keep up the great work!")
    else:
        print("\n❌ Failed to create entry.")
        sys.exit(1)


if __name__ == "__main__":
    main()
