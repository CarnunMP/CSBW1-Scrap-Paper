import tracery
from tracery.modifiers import base_english

rules = {
    'name': ['corridor'],
    'adjective': ['dark', 'smoky', 'dangerous-looking', 'messy'],
    'adverb': ['suspiciously', 'strangely', 'worryingly'],
    'setTitleType': ['#adjective.capitalize#', '#adverb.capitalize# #adjective.capitalize#'],
    'title': '#setTitleType# #name.capitalize#',
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

rooms = []
for i in range(10):
    rooms.append(grammar.flatten('#title#'))

print(rooms)