from common import Arc, Constituent
from example2 import rules, words, dictionary

chart = []

def add_to_chart(arc):
    for i in chart:
        if i.rule.rule_id != arc.rule.rule_id:
            continue
        if i.start != arc.start:
            continue
        if i.end != arc.end:
            continue
        if len(i.constituents) != len(arc.constituents):
            continue
        for j in range(len(i.constituents)):
            if i.constituents[j] != arc.constituents[j]:
                continue
        return
    chart.append(arc)
    arc.show()

agenda = []
current = 0
while current < len(words) or len(agenda) > 0:
    if len(agenda) == 0:
        word = [i for i in dictionary if i.word == words[current]][0]
        for i in word.tag:
            agenda.append(Constituent(i, current+1, current+2))
        current += 1
    constituent = agenda.pop()
    for i in rules:
        if constituent.tag == i.target[0] and len(i.target) > 1:
            add_to_chart(Arc(i, 1, constituent.start, constituent.end, [constituent.constituent_id]))
        if constituent.tag == i.target[0] and len(i.target) == 1:
            agenda.append(Constituent(i.source, constituent.start, constituent.end, i, [constituent.constituent_id]))
    for i in chart:
        if constituent.start != i.end:
            continue
        if constituent.tag == i.rule.target[i.current] and i.current+1 != len(i.rule.target):
            add_to_chart(Arc(i.rule, i.current+1, i.start, constituent.end, i.constituents + [constituent.constituent_id]))
        if constituent.tag == i.rule.target[i.current] and i.current+1 == len(i.rule.target):
            agenda.append(Constituent(i.rule.source, i.start, constituent.end, i.rule, i.constituents + [constituent.constituent_id]))
