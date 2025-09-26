# import random
# import string

# def generate_password(length, uppercase, lowercase, numbers, special):
#     """
#     Generates a password with customizable options for length, complexity, and character types.
#     """

#     # Define the character sets for each type of character
#     uppercase_chars = string.ascii_uppercase if uppercase else ''
#     lowercase_chars = string.ascii_lowercase if lowercase else ''
#     number_chars = string.digits if numbers else ''
#     special_chars = string.punctuation if special else ''

#     # Combine the character sets into a single pool of possible characters
#     possible_chars = uppercase_chars + lowercase_chars + number_chars + special_chars

#     # Ensure the length of the password is at least 8 characters
#     length = max(length, 8)

#     # Generate the password
#     password = ''.join(random.choice(possible_chars) for i in range(length))

#     # Save the password to a file
#     with open('passwords.txt', 'a') as f:
#         f.write(password + '\n')

#     return password


# # Example usage
# password = generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special=True)
# print(password)


# 30 days money doubling calculation
# Each day the amount gets MULTIPLIED by 2 (not added)

# Method 1: Simple Loop approach - showing step by step multiplication


# 🛒 SHOPPING MALL PROJECT - TWO SUM CONCEPT
# Real life example: Dui ta item kinte hobe jetar total = budget
