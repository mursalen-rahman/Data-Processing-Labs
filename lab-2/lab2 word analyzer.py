text = input("Enter a word or short sentence: ")

num_characters = len(text)
vowel_count = 0
space_count = 0

# Check each character
for char in text:
    if char in "aeiouAEIOU":
        vowel_count = vowel_count + 1
    elif char == " ":
        space_count = space_count + 1

# Display results
print("Total characters:", num_characters)
print("Total vowels:", vowel_count)
print("Total spaces:", space_count)