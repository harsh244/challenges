from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    file=open(DICTIONARY,'r')
    k=file.read()
    return k.split('\n')
    pass


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score =0
    for letter in word:
        score=score+LETTER_SCORES.get(letter.upper(),0)
    return score
    
    pass

def max_word_value(line):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    maxx=0
    maxword=''
    for word in line:
        if calc_word_value(word)>maxx:
            maxword=word
    
    return maxword        
    pass

if __name__ == "__main__":

    pass # run unittests to validate
