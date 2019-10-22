from common import Rule, Word

rules = []
rules.append(Rule('S', 'NP VP'))
rules.append(Rule('NP', 'N'))
rules.append(Rule('NP', 'SURNAME N'))
rules.append(Rule('NP', 'N N'))
rules.append(Rule('NP', 'V N'))
rules.append(Rule('PP', 'PREP NP'))
rules.append(Rule('VP', 'V NP'))
rules.append(Rule('VP', 'ADV VP'))
rules.append(Rule('VP', 'PP VP'))

words = '王 翻译 在 翻译 小说'
words = words.split()
dictionary = []
dictionary.append(Word('王', 'SURNAME N'))
dictionary.append(Word('翻译', 'N V'))
dictionary.append(Word('在', 'V ADV PREP'))
dictionary.append(Word('小说', 'N'))

if __name__ == '__main__':
    for i in rules:
        print(i)

    print()

    for i in dictionary:
        print(i)
