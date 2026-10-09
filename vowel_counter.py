word = input("Enter a word to count vowels for: ")
vowels = ['a','e','i','o','u']
letters = word.split(vowels)

for letter in letters:
    print(letter)
    if letter in vowels:
        vowel_total = vowel_total+1
        print(f"there are {vowel_total} vowels")
