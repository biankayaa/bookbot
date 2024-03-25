import os

path = '~/workspace/github.com/biankayaa/bookbot/books/frankenstein.txt'
expanded_path = os.path.expanduser(path)

with open(expanded_path, 'r') as file:
    content = file.read()
    print(content)

print(

)
print("--- Begin report of books/frankenstein.txt ---")

def count_words(frankenstein):
    try:
        with open(expanded_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        return word_count
    except FileNotFoundError:
        print(f"File '{frankenstein}' not found.")
        return 0

total_words = count_words(path)
print(f"{total_words} words found in the document")

print(

)

def sort_on(character_dict):
    return character_dict['count']

def count_characters(frankenstein):
    characters = {}
    for char in frankenstein:
        lower = char.lower()
        if lower.isalpha():
            if lower in characters:
                characters[lower] += 1
            else:
                characters[lower] = 1
    result_char = [{'char': char, 'count': count} for char, count in characters.items()]
    result_char.sort(reverse=True, key=sort_on)
    return result_char

def print_report(sorted_chars):
    for char_dict in sorted_chars:
        char = char_dict['char']
        count = char_dict['count']
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

sorted_chars = count_characters(path)
print_report(sorted_chars)




