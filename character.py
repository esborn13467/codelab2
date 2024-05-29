def checkchar(character):
    vowels = 'aeiou'
    if character in vowels:
        print("Character is a vowel")
    else:
        print("Character is not a vowel")
character = input("Enter a character: ")

print (checkchar(character.lower()))