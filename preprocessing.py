import unidecode
import re

def preprocessing(word: str):
    word = word.lower()
    word = unidecode.unidecode(word)
    word = word.replace('"',' ASPAS ')
    word = re.sub(r'\d\S+', ' 0 ', word)
    word = re.sub(r'\d+', '0', word)
    word = re.sub(r'http\S+', ' URL ', word)
    word = re.sub(r'\S+@\S+', 'EMAIL', word)
    word = re.sub(r'\s@\S+', ' REDESOCIAL ', word)
    word = re.sub(r'[^\w\s]', '', word)
    word = ' '.join(word.split())
    return word