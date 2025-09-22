#print("hello")
def get_book_text(book_filepath):
    with open(book_filepath) as file:
        book_as_string = file.read()
    return book_as_string

path = "books/frankenstein.txt"
wordlist = []
wordcount = 0
def word_counter(book_filepath):
    text1 = get_book_text(book_filepath)
    wordlist = text1.split()
    #print(wordlist)
    wordcount = len(wordlist)
    return wordcount
def main():
    print(f"{word_counter(path)} words found in the document")
    #text1 = get_book_text(path)
    #print(text1)


main()