import string
def cleanText(text):
    mistakes = 0
    for letter in text:
        if((letter not in string.ascii_letters+' ')or(len(text)>30)):
            mistakes +=1
    return mistakes
