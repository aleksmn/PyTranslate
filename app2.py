# English Dictionary App
# Getting data from MySQL database

import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

# Get all keys

cursor.execute('SELECT Expression FROM Dictionary')
keys = []
for i in cursor.fetchall():
    keys.append(i[0])

def translate(w):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    if results:
        return results
    elif len(get_close_matches(w, keys)) > 0:
        match = get_close_matches(w, keys)[0]
        yn = (input(f'Did you meen "{match}"? (Y/N) ')).upper()
        if yn == 'Y':
            cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{match}'")
            return cursor.fetchall()
        elif yn == 'N':
            return 'The word does not exists.'
        else:
            return 'We did not understand your query.'
    else:
        return 'The word does not exists!'


print('\n'
      '==========================\n'
      'Welcome to our dictionary!\n'
      '         Version 2        \n'
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
                print(i[1])
        else:
            print(output)
except KeyboardInterrupt as e:
    print('\nProgramm interrupted. Bye!')