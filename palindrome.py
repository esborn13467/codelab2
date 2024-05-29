import re


def is_palindrome(s):
    # Normalize the input string
    s = s.lower()  # Convert to lowercase
    s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
s=input("enter a string")
is_palindrome(s)


