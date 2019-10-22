from common import Arc, Constituent
from example2 import rules, words, dictionary

chart = []

def top_down_arc_introduction_algorithm(arc):
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
    for i in rules:
        if i.source == arc.rule.target[arc.current]:
            top_down_arc_introduction_algorithm(Arc(i, 0, arc.end, arc.end))

for i in rules:
    if i.source == 'S':
        top_down_arc_introduction_algorithm(Arc(i, 0, 1, 1))

agenda = []
current = 0
while current < len(words) or len(agenda) > 0:
    if len(agenda) == 0:
        word = [i for i in dictionary if i.word == words[current]][0]
        for i in word.tag:
            agenda.append(Constituent(i, current+1, current+2))
        current += 1
    constituent = agenda.pop()
    for i in chart:
        if constituent.start != i.end:
            continue
        if constituent.tag == i.rule.target[i.current] and i.current+1 != len(i.rule.target):
            top_down_arc_introduction_algorithm(Arc(i.rule, i.current+1, i.start, constituent.end, i.constituents + [constituent.constituent_id]))
        if constituent.tag == i.rule.target[i.current] and i.current+1 == len(i.rule.target):
            agenda.append(Constituent(i.rule.source, i.start, constituent.end, i.rule, i.constituents + [constituent.constituent_id]))
