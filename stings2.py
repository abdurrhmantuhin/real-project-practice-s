from datetime import datetime
import random

print("📔 Welcome to Your Personal Diary Manager!")
print("Welcome to Your Personal Diary Manager!")
print("=" * 55)

print("\n📝 1. DIARY ENTRY CREATION - Creating Diary Entries")
print("-" * 50)


today_date = "2025-11-21"
user_name = "tuhin"
mood = "happy"

entry1 = 'today was a very good day'

entry2 = "my friend said to me, your very good student"

long_entry = """to day was a very special day
wento to university in the morning.
had a chat friend in the afternoon
had dinner with family at night. 
""".title()

diary_location = r'C:\Users\GOAT TUHIN\Desktop'

print(f"📅 Date: {today_date}")
print(f"👤 User: {user_name}")
print(f"😊 Mood: {mood}")
print(f"📝 Short entry: {entry1}")
print(f"💬 Quote entry: {entry2}")
print(f"📖 Long entry:\n{long_entry}")
print(f"💾 Saved at: {diary_location}")


print(f"\nEntry lengths:")
print(f"Short entry: {len(entry1)} characters")
print(f"Long entry: {len(long_entry)} characters")


print("\n✂️ 2. EXTRACTING INFO FROM ENTRIES - Extracting Information from Entries")
print("-" * 60)

diary_text = "today i went to dhaka university and met my friend samrat"
print(f"full entry: {diary_text.title()}")

print(f"First word:{diary_text[:5]}")
print(f"Last word: '{diary_text[-5:]}'")
print(f"University part: '{diary_text[19:34]}'")           
print(f"Every 2nd character: '{diary_text[::2]}'")         
print(f"Reverse reading: '{diary_text[::-1]}'") 

date_string = "2024-01-15"
print(f"\nDate analysis of '{date_string}':")
print(f"Year: '{date_string[:4]}'")
print(f"Month: '{date_string[5:7]}'")        
print(f"Day: '{date_string[8:10]}'")         
print(f"Month-Day: '{date_string[5:]}'") 

time_string = "14:30:45"
print(f"\nTime analysis of '{time_string}':")
print(f"Hour: '{time_string[:2]}'")          
print(f"Minute: '{time_string[3:5]}'")       
print(f"Second: '{time_string[6:]}'")       


print("\n🧹 3. CLEANING & MODIFYING ENTRIES - Cleaning and Modifying Entries")
print("-" * 65)

messy_entry = " i WENT to school TODAY and had fun with friends "
print(F"messy entry: {messy_entry}")
step1 = messy_entry.strip()
step2 = messy_entry.lower()
step3 = messy_entry.capitalize()
step4 = messy_entry.title()
step5 = messy_entry.upper()
step6 = messy_entry.swapcase()

print(f"After strip():'{step1}'")
print(f"After lower(): '{step2}'")
print(f"After capitalize(): '{step3}'")
print(f"After title(): '{step4}'")
print(f"After upper(): '{step5}'")
print(f"After swapcase(): '{step6}'")

old_entry = "I hate studying math"
new_entry1 = old_entry.replace("hate","love")
new_entry2 = old_entry.replace("math","programming")
entry3 = old_entry.replace("hate","love").replace("math","programming").replace("studying","learn")
print(f"\nEntry fixing:")
print(f"Original: '{old_entry}'")
print(f"Fix 1: '{new_entry1}'")
print(f"Fix 2: '{new_entry2}'")
print(f"Both fixed: '{entry3}'")


bad_words = ["bad", "boring", "terrible"]
good_entry = "Today was bad and boring, really terrible day"
print(f"\nPositivity filter:")
print(f"befor: {good_entry}")

for bad_word in bad_words:
    if bad_word == "bad":
        good_entry = good_entry.replace(bad_word, "good")
    elif bad_word == "boring":
        good_entry = good_entry.replace(bad_word, "exciting")  
    elif bad_word == "terrible":
        good_entry = good_entry.replace(bad_word, "amazing")

print(f"After: '{good_entry}'")


print("\n🔗 4. BUILDING DIARY ENTRIES - Building Diary Entries")
print("-" * 55)
