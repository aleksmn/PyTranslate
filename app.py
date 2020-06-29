# English Dictionary App
# Getting data from local JSON file

import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        match = get_close_matches(w, data.keys(), cutoff=0.8)[0]
        yn = (input(f'Did you meen "{match}"? (Y/N) ')).upper()
        if yn == 'Y':
            return data[match]
        elif yn == 'N':
            return 'The word does not exists.'
        else:
            return 'We did not understand your query.'
    else:
        return 'The word does not exists.'


print('\n'
      '==========================\n'
      'Welcome to our dictionary!\n'
      '         Version 1        \n'
      '        (q to quit)       \n'
      '==========================')

try:
    while True:
        word = (input('\nEnter a word: '))

        if word.lower() == 'q':
            print('Thank you! Bye-bye!')
            break

        output = translate(word)

        if isinstance(output, list):
            for i in output:
                print(i)
        else:
            print(output)
except KeyboardInterrupt as e:
    print('\nProgramm interrupted. Bye!')
