def myFunction(word, word_list):

    sorted_word = sorted(word.lower())
    anagramList = list(filter(lambda w: sorted(w.lower()) == sorted_word, word_list))

    return anagramList

