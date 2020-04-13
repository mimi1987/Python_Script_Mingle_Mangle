from random import choice

def shuffle_letters(word):
    letter_list = list(word)
    for _ in range(100):
        result_list = []
        for _ in range(len(letter_list)):
            char = choice(letter_list)
            result_list.append(char)
        res = ''.join(result_list)
        print(res)

word = input('Please enter a word: ')

shuffle_letters(word)
