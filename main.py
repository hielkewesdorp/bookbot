#print("hello")
from stats import get_book_text
from stats import word_counter
from stats import character_counter
path = "books/frankenstein.txt"





def main():
    character_counter(path)
    print(f"{word_counter(path)} words found in the document")
    characterlist = character_counter(path)
    print(characterlist)
    #text1 = get_book_text(path)
    #print(text1)


main()