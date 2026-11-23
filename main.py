def remove_vowels(document):
    new_string = ""
    vowels = "aeiouyAEIOUY"
    for char in document:
        if char not in vowels:
            new_string += char
    return new_string
print(remove_vowels("Hello World!"))



