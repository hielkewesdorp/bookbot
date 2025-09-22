#print("hello")
import sys
from stats import get_book_text
from stats import word_counter
from stats import character_counter
from stats import character_sorter
#path = "books/frankenstein.txt"

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]



def main():
    #print(f"{word_counter(path)} words found in the document")
    characterlist = character_counter(path)
    #print(characterlist)
    #print(type(characterlist))
    #text1 = get_book_text(path)
    #print(text1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(path)} total words")
    print("--------- Character Count -------")
    sortedlist = character_sorter(characterlist)
    #print(sortedlist)
    for entries in sortedlist:
        if entries["char"].isalpha() == False:
            continue
        else:
            print(f"{entries["char"]}: {entries["num"]}")
    print("============= END ===============")
main()