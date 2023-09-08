input_string = 'I love Python'
char_count = {}

for char in input_string:
    if char.isalpha():
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
print(char_count)
