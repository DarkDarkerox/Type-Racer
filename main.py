import random
import msvcrt
import os


def make_paragraph(book_words):
    text = []
    for i in range(48):
        index = random.randint(0, len(words))
        text.append(words[index])
    index = 0
    for j in range(4):
        for i in range(12):
            print(text[index], end=" ")
            index += 1
        print()
    return text

def type_check(test):
    print("-" * 50)
    for line in range(4):
        for word in test[line * 12 : 12 + line * 12]:
            index = 0
            while index < len(word):
                caracter = msvcrt.getwch()
                if caracter == word[index]:
                    print(caracter, end="", flush=True)
                    index += 1
            print(end=" ")
        print()
    os.system('cls' if os.name == 'nt' else 'clear')

book_name = 'book.txt'

try:
    with open('book.txt', encoding='utf-8') as book:
        contents = book.read()
except FileNotFoundError:
    print("File {} is not in this folder".format(book_name))
else:
    words = contents.split()

while True:
    text = make_paragraph(words)
    type_check(text)

