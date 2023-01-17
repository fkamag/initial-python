def append_each_letter_of_the_word_in_a_list(word):
    return [letter for letter in word]


def return_index_of_the_uppercase_letter(word):
    for index, letter in enumerate(word):
        if letter.isupper():
            return index


def return_element_from_list_that_is_string(input_list):
    for element in input_list:
        if type(element) is str:
            return element
