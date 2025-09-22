#print("hello")
def get_book_text(book_filepath):
    with open(book_filepath) as file:
        book_as_string = file.read()
    return book_as_string

path = "books/frankenstein.txt"

def main():
    text1 = get_book_text(path)
    print(text1)

main()