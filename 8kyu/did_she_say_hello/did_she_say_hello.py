import re

def validate_hello(greetings):
    
    lst = ['hello','ciao','salut','hallo','hola','ahoj','czesc']

    for word in greetings.split():
        word = "".join(re.split("[^a-zA-Z]*", word))
        if word.lower() in lst:
            return True
    return False

