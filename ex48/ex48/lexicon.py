from ex48 import ex48_convert as e

#lists of okay words
direction = ['north', 'south', 'east', 'west']
verbs = ['go', 'stop', 'fight', 'eat', 'open', 'use']
stopWords = ['the', 'in', 'from', 'at']
nouns = ['door', 'princess', 'bear']

#scan over user input for lexicon words and return them in tuples
def scan(stuff):
    #takes input, coverts it to lower case and seprates
    #each word and places them on the words list 
    words = stuff.lower().split()
    results = []

    for i in words:
        if i in direction:
            results.append(('direction', i))
        elif i in verbs:
            results.append(('verb', i))
        elif i in stopWords:
            results.append(('stops', i))
        elif i in nouns:
            results.append(('noun', i))
        elif i.isdigit():
            results.append(('num', e.convert_number(i)))
        else:
            results.append(('error', i))
    return results
