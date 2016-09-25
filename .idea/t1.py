

def break_words(stuff):
    # This function will break up words for us
    words = stuff.split(' ')
    return words

def sort_words(words):
    # sort the words
    return sorted(words)

def print_first_words(words):
    # prints the first words that pop
    word = words.pop()
    print word

def print_last_words(words):
    # prints the last words after popping it off
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first and last words of the sentence"""
    words = break_words(sentence)
    print print_first_words(words)
    print print_last_words(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)



