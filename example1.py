from common import Rule, Word

rules = []
rules.append(Rule('S', 'NP VP'))
rules.append(Rule('NP', 'ART ADJ N'))
rules.append(Rule('NP', 'ART N'))
rules.append(Rule('NP', 'ADJ N'))
rules.append(Rule('VP', 'AUX VP'))
rules.append(Rule('VP', 'V NP'))

words = 'the large can can hold the water'
words = words.split()

dictionary = []
dictionary.append(Word('the', 'ART'))
dictionary.append(Word('large', 'ADJ'))
dictionary.append(Word('can', 'N AUX V'))
dictionary.append(Word('hold', 'N V'))
dictionary.append(Word('water', 'N V'))

if __name__ == '__main__':
    for i in rules:
        print(i)

    print()

    for i in dictionary:
        print(i)
