def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    character_dict = {}
    text_list = []

    text_list = list(book_text)
    for word in text_list:
        for character in word.split():
            lower_case_char = character.lower()

            if lower_case_char in character_dict:
                character_dict[lower_case_char] += 1
            else:
                character_dict[lower_case_char] = 1
    
    return character_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list