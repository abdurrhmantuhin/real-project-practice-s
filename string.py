print("let's start learning python strings!!!")
print("=" * 39)

print("\n1. string basics - how to creat strings")
print("=" * 40)

name1 = 'My Name Is Tuhin'
name2 = "My Name Is Rhman"
address = """ House Address:
Dhaka, Bangladesh!
"""
print(f"with single quotes:{name1}")
print(f"with duble quote:{name2}")
print("multi-line string: ")
print(address)

print(f"length of  '{name1}': {len(name1)} charecters")
print(f"length of  '{name2}': {len(name2)} charecters")




print("\n2. starting slicing - string slicing")
print("=" * 38)

text = "Python programing"
print(f"our text '{text}'")

print(f"First 6 charecters: '{text[:6]}' ")
print(f"Last 10 charecters: '{text[-10:]}' ")
print(f"From middle (7-18): '{text[7:18]}' ")
print(f"Reversed: '{text[::-1]}' ")
print(f"Every 2nd charecters: '{text[::2]}'")

word = "Bangladesh"
print(f"\nnew word: '{word}'")
print(f"fist 5 charecters: '{word[:5]}'")
print(f"last 4 charecters: '{word[-4:]}'")
print(f"middle: '{text[2:6]}'")




print("\n3. string modification")
print("=" * 40)

messy_text = " HELLO world "
print(f"Original text:{messy_text}")

clean_text = messy_text.strip()
lower_text = clean_text.lower()
upper_text = clean_text.upper()
tilte_text = clean_text.title()
capital_text = clean_text.capitalize()

print(f"after strip: {clean_text}")
print(f"after lower: {lower_text} ")
print(f"after uppar: {upper_text} ")
print(f"after title: {tilte_text} ")
print(f"after captitalize: {capital_text} ")

old_sentence = "I love cats"
new_sentence = old_sentence.replace("cats","dogs")
print(f"\nbefor replce: {old_sentence}")
print(f"after replce: {new_sentence}")




print("\n4. string concatenation ")
print("=" * 40)

first_name = "tuhin"
last_name = "kazi"
age = 20

full_name1 = first_name + " " + last_name
print(F"using '+' : {full_name1}")

full_info = f"Name: {first_name} {last_name}, age: {age}s "
print(F"using f string: {full_info}")

full_info2 = "name: {} {} age: {}".format(first_name,last_name,age)
print(F"using 'format()':{full_info2}") 

words = ["I", "LIVE", "IN", "BANGLADESH"]
sentence = " ".join(words)
print(F"using 'join()': {sentence}")

print("\n5. Beautiful formatting")
print("-" * 40)

name =  "Abdur"
marks = 86.92
percentage = 98.6565

print(F"student name: {name}")
print(F"student marks: {marks}")
print(F"percentage: {percentage:.1f}")
print(F"marks: {marks:.1f}")

big_number =  1234567
print(f"big number: {big_number}")

text = "python"
print(F"left aligned: '{text:<20}'")
print(F"right aligned: '{text:>20}'")
print(F"center aligned: '{text:^20}'")
