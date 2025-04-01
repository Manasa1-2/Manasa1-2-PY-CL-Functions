# lab.py

def count_vowels(string):
    vowels = "aeiouAEIOU"
    c = 0
    for char in string:
        if char in vowels:
            c += 1
    return c