import random
import os


def read_data(filepath="./files/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath="./files/data.txt")
    chose_word = random.choice(data)
    chose_word_list = [letter for letter in chose_word]
    chose_word_list_underscores = ["_"] * len(chose_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chose_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("cls")
        print("!Adivina la palabra!")
        for element in chose_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingres una letra: ").strip().upper()
        assert letter.isalpha(), "solo puedes ingresar letras"

        if letter in chose_word_list:
            for idx in letter_index_dict[letter]:
                chose_word_list_underscores[idx] = letter

        if "_" not in chose_word_list_underscores:
            os.system("cls")
            print("Ganaste! La palabara era: ", chose_word)
            break


if __name__ == '__main__':
    run()
