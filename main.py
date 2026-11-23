def count_consonants(text):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count
print(count_consonants("Hello World"))




