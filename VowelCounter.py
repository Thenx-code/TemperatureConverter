# Vowel Counter
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
x = 0
word = input("Enter a word: ").lower()
letter_count = len(word)

while x < letter_count:
    if word[x] in vowels:
       vowel_count += 1
       x += 1

    else:
       vowel_count = vowel_count
       x += 1

print(f"The number of vowels in the word is {vowel_count}")



