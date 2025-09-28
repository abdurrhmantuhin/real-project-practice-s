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

name  = "arny"
age = 18
location = "Dhaka"
activity = "GYM"
feelings = "well"

entry_plus = "my name is :" + name + "| my age is: " + str(age) + "years"
print(f"'+'oparetors: {entry_plus}")

entry_fstring = f"my naame is {name}, and my age is: {age} age, im living in {location} and today im going to {activity} now i feel so {feelings} !!!"
print(f"f-string: {entry_fstring}")


entry_format = "my name is{}, age: {}, i live in: {} and today my mood is{}".format(name,age,location,feelings)
print(F"'.format()' format: {entry_format}")


entry_parts = {
    f"date: {datetime.now().strftime('%Y-%m-%d')}",
    f"name {name}",
    f"today work: {activity}",
    f"feelings: {feelings}"
}

entry_joined = "|".join(entry_parts)
print(entry_joined)


print(f"\n📖 Complete Diary Entry:")
complete_entry = f"""
{"="*40}
date:{datetime.now().strftime('%B %d, %Y')}
writer : {name}
location: {location}
mood: {feelings}
{"=" * 40}

to day i feel {feelings}
and i spend more time in {activity}
feeling well bc im living in {location}..
{'='*40}
"""

print(complete_entry)



print("\n📊 ৫. BEAUTIFUL DIARY FORMATTING - সুন্দর ডায়েরি ফরম্যাটিং")
print("-" * 60)

writer = "tuhin"
score = 87.5
words_written = 1234
time_spent = 2.5

print("📈 Writing Statistics:")
print(f"writer: {writer}")
print(f"score:{score:.1f}")
print(f"words writen: {words_written}")
print(f"time spent: {time_spent:.2f}")

print(f"\n📋 Diary Summary Report:")
print(F"{'writer':<10}:{writer}")
print(F"{'score':<10}: {score:.2f}")
print(F"{'words':<10}: {words_written:.2f}")
print(F"{'with':<10}: {time_spent}")


completion = 0.875
print(f"\ncompletion: {completion:.1%}")
print(f"padded numnber: {42:0>5}")
print(f"righ aliged: {writer:>20}")
print(f"cntered:{writer:^29}")
print(f"with start: {writer:*^20}")

now = datetime.now()
print(f"\n🕒 Time Formats:")
print(f"Full date: {now:%A, %B %d, %Y}")
print(f"Short date: {now:%d/%m/%Y}")
print(f"Time: {now:%H:%M:%S}")
print(f"12-hour: {now:%I:%M %p}")

print("\n🚨 6. SPECIAL CHARACTERS IN DIARY ")
print("-" * 55)

diary_quote = "My \"mother \"Focus \"on \"your \"studies.\" I said, 'Okay, mother.'"
print(F"quotes exmple: {diary_quote}")

formatted_diary = """Today's diary:
\t• Woke up at 7 am
\t• Had breakfast
\t• Went to school
\t• Played in the afternoon"""

print(f"Formatted entry:\n{formatted_diary}")


windows_path = "C:\\Users\\Documents\\MyDiary\\today.txt"
linux_path = "/home/user/documents/diary/today.txt"
raw_windows = r"C:\Users\Documents\MyDiary\today.txt"

print(f"\nFile paths:")
print(f"Windows: {windows_path}")
print(f"Linux: {linux_path}")  
print(f"Raw string: {raw_windows}")
