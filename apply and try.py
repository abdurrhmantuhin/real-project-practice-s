print("\n📝 Exercise 2: Word Counter")
def count_words(text):
    """Count words"""
    words = text.split()
    return len(words)

sentences = [
    "I eat rice",
    "How are you today", 
    "Bangladesh is our beloved country"
]

print("Word counting:")
for sentence in sentences:
    word_count = count_words(sentence)
    print(f"'{sentence}' -> {word_count} words")