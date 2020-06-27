import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def get_match(word):
    return get_close_matches(word, data.keys(), cutoff=0.8)[0]

def translate(word):
    if word in data:
        return data[word]
    elif get_match(word):
        yn = (input(f'Did you meen "{get_match(word)}"? (Y/N) ')).upper()
        if yn == 'Y':
            return data[get_match(word)]
        elif yn == 'N':
            return 'The word does not exists.'
        else:
            return 'We did not understand your query.'
    else:
        return 'The word does not exists.'

word = (input('Enter word: ')).lower()

output = translate(word)

if isinstance(output, list):
    for i in output:
        print(i)
else:
    print(output)