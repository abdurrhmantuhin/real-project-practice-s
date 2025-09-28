# print("let's start learning python strings!!!")
# print("=" * 39)

# print("\n1. string basics - how to creat strings")
# print("=" * 40)

# name1 = 'My Name Is Tuhin'
# name2 = "My Name Is Rhman"
# address = """ House Address:
# Dhaka, Bangladesh!
# """
# print(f"with single quotes:{name1}")
# print(f"with duble quote:{name2}")
# print("multi-line string: ")
# print(address)

# print(f"length of  '{name1}': {len(name1)} charecters")
# print(f"length of  '{name2}': {len(name2)} charecters")




# print("\n2. starting slicing - string slicing")
# print("=" * 38)

# text = "Python programing"
# print(f"our text '{text}'")

# print(f"First 6 charecters: '{text[:6]}' ")
# print(f"Last 10 charecters: '{text[-10:]}' ")
# print(f"From middle (7-18): '{text[7:18]}' ")
# print(f"Reversed: '{text[::-1]}' ")
# print(f"Every 2nd charecters: '{text[::2]}'")

# word = "Bangladesh"
# print(f"\nnew word: '{word}'")
# print(f"fist 5 charecters: '{word[:5]}'")
# print(f"last 4 charecters: '{word[-4:]}'")
# print(f"middle: '{text[2:6]}'")




# print("\n3. string modification")
# print("=" * 40)

# messy_text = " HELLO world "
# print(f"Original text:{messy_text}")

# clean_text = messy_text.strip()
# lower_text = clean_text.lower()
# upper_text = clean_text.upper()
# tilte_text = clean_text.title()
# capital_text = clean_text.capitalize()

# print(f"after strip: {clean_text}")
# print(f"after lower: {lower_text} ")
# print(f"after uppar: {upper_text} ")
# print(f"after title: {tilte_text} ")
# print(f"after captitalize: {capital_text} ")

# old_sentence = "I love cats"
# new_sentence = old_sentence.replace("cats","dogs")
# print(f"\nbefor replce: {old_sentence}")
# print(f"after replce: {new_sentence}")




# print("\n4. string concatenation ")
# print("=" * 40)

# first_name = "tuhin"
# last_name = "kazi"
# age = 20

# full_name1 = first_name + " " + last_name
# print(F"using '+' : {full_name1}")

# full_info = f"Name: {first_name} {last_name}, age: {age}s "
# print(F"using f string: {full_info}")

# full_info2 = "name: {} {} age: {}".format(first_name,last_name,age)
# print(F"using 'format()':{full_info2}") 

# words = ["I", "LIVE", "IN", "BANGLADESH"]
# sentence = " ".join(words)
# print(F"using 'join()': {sentence}")




# print("\n5. Beautiful formatting")
# print("=" * 40)

# name =  "Abdur"
# marks = 86.92
# percentage = 98.6565

# print(F"student name: {name}")
# print(F"student marks: {marks}")
# print(F"percentage: {percentage:.1f}")
# print(F"marks: {marks:.1f}")

# big_number =  1234567
# print(f"big number: {big_number}")

# text = "python"
# print(F"left aligned: '{text:<20}'")
# print(F"right aligned: '{text:>20}'")
# print(F"center aligned: '{text:^20}'")




# print("\n6. ESCAPE CHARACTERS ")
# print("=" * 40)

# print("first line\nsecond line ")

# print("name\trahman")
# print("age:\t25")

# print('He said, "i am fine"')
# print("He said, 'i am fine'")

# file_path = r"c://user//desktop//file.txt"
# print(f"file path: {file_path}")

# raw_path = r"c://user//desktop//file.txt"
# print(f"raw string: {raw_path}")




# print("\n7. STRING METHODS ")
# print("=" * 40)

# sample = "Hello python world"
# print(f"sample taxt: {sample}")

# print(f"isalpha() (all latters?): {'hello'.isalpha()}")
# print(f"isdigit() (all number?): {'123'.isdigit()}")
# print(f"islower() (all lowercase?): {"hello".islower()}")
# print(f"isupper() (all uppercase?): {"HELLO".isupper()}")

# print(F"find ('python) : {sample.find('python')}")
# print(F"count('l'): {sample.count('l')}")
# print(F"startwith('hello'): {sample.startswith('Hello')}")
# print(F"endwith('world'): {sample.endswith('world')}")

# sentences = "i eat rice every day"
# words = sentences.split()
# print(F"after split: {words}")

# rejoined = "=".join(words)
# print(f"rejoined: {rejoined}")




# print("\n8. PRACTICAL EXERCISES")
# print("=" * 50)

# print("\nexercise 1: name formatter")
# def format_name(name):
#     clean_name =  name.strip().title()
#     return clean_name

# names = ["tuhin", "arny", "ayra"]
# print("name formating!!!")
# for name in names:
#     formatted = format_name(name)
#     print(F"befor:{name} ---- after:{formatted}")


# print("\nexercise 2: Word counter")
# def count_word(text):
#     words = text.split()
#     return len(words)

# sentences = [
#     "I eat rice",
#     "How are you today", 
#     "Bangladesh is our beloved country"
# ]

# print("word counting:....")
# for santance in sentences:
#     word_count = count_word(santance)
#     print(F"befor sentence: {santance} ---- after sencence: {word_count}")
    
# print("\nexercise 3: simple email check")
# def check_email(email):
#     email =  email.strip().lower()
#     if "@" in email and "." in email:
#         return "looks valid"
#     else:
#         return "looks invalid"
    
# emails = ["user@gmail.com", "invalid.email", "test@yahoo.com"]
# print("email checking:")
# for email in emails:
#     results = check_email(email)
#     print(f"                 my email is: {email} ---- status: {results}")



# print("\n exercise 4: text statistiics")
# def text_stats(text):
#     char_count = len(text)
#     char_no_space = len(text.replace(" ",""))
#     word_count = len(text.split())

#     return {
#         "characters" : char_count,
#         "characters_no_space" : char_no_space,
#         "word" : word_count
#     }

# semple_text = "Python in easays programing"
# stats = text_stats(semple_text)
# print(F"text: {semple_text}")
# print(F"total charecter: {stats['characters']}")
# print(f"charecter withour space: {stats['characters_no_space']}")
# print(F"total word: {stats['word']}")
# print("print")