import re


def is_palindrome(s):
    # Normalize the input string
    s = s.lower()  # Convert to lowercase
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
s=input("enter a string")
is_palindrome(s)


