class Word:
    def __init__(self, word, tag):
        self.word = word
        self.tag = tag.split()

    def __str__(self):
        return '%s : %s' % (self.word, ' '.join(self.tag))

class Rule:
    count = 0

    def __init__(self, source, target):
        Rule.count += 1
        self.rule_id = Rule.count
        self.source = source
        self.target = target.split()

    def __str__(self):
        return '%s -> %s' % (self.source, ' '.join(self.target))

class Arc:
    def __init__(self, rule, current, start, end, constituents=None):
        self.rule = rule
        self.current = current
        self.start = start
        self.end = end
        self.constituents = constituents if constituents else []

    def show(self):
        print('arc,', self.rule.rule_id, ',', self.start, ',', self.end, ',', '&'.join([str(i) for i in self.constituents]), ',')

    def __str__(self):
        return '%s -> %s ^ %s' % (self.rule.source, ' '.join(self.rule.target[:self.current]), ' '.join(self.rule.target[self.current:]))

class Constituent:
    count = 0

    def __init__(self, tag, start, end, rule=None, constituents=None):
        Constituent.count += 1
        self.constituent_id = Constituent.count
        self.tag = tag
        self.start = start
        self.end = end
        self.rule = rule
        self.constituents = constituents if constituents else []
        print('constituent,', tag, ',', start, ',', end, ',', self.constituent_id, ',', rule.rule_id if rule else '', ',' ,'&'.join([str(i) for i in self.constituents]), ',')

    def show(self):
        print('DEBUG: constituent,', self.tag, ',', self.start, ',', self.end, ',', self.constituent_id, ',', self.rule.rule_id if self.rule else '', ',' ,'&'.join([str(i) for i in self.constituents]), ',')
