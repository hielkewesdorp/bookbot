def get_book_text(book_filepath):
    with open(book_filepath) as file:
        book_as_string = file.read()
    return book_as_string

def word_counter(book_filepath):
    wordlist = []
    wordcount = 0
    text1 = get_book_text(book_filepath)
    wordlist = text1.split()
    #print(wordlist)
    wordcount = len(wordlist)
    return wordcount

def character_counter(book_filepath):
    worldlist = []
    text1 = get_book_text(book_filepath)
    text2 = text1.lower()
    wordlist = text2.split()
    #print(wordlist)
    letterlist = set()
    for words in wordlist:
        for letters in words:
            letterlist.add(letters) #create set of unique characters
    #print(letterlist)
    letter_dictionary = {}
    for letters in letterlist:
        letter_dictionary[letters] = 0 #create dictionary of characters and count zero
    #print(letter_dictionary)
    for words in wordlist:
        for letters in words:
            letter_dictionary[letters] += 1 #count the number of times of each character in the file
    #print(letter_dictionary)
    return letter_dictionary





