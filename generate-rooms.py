import tracery
from tracery.modifiers import base_english

rules = {
    'roomName': ['room', 'corridor', 'medbay', 'armoury', 'quarters', 'bridge', 'brig', 'passageway', 'laboratory', 'mess-hall', 'engine-room'],
    'adjective': ['dark', 'smoky', 'dangerous-looking', 'messy', 'quiet', 'irradiated', 'full', 'empty', 'packed', 'stripped', 'ransacked'],
    'adverb': ['suspiciously', 'strangely', 'worryingly', 'puzzlingly', 'suprisingly', 'curiously'],
    'setTitleType': ['#adjective.capitalize#', '#adverb.capitalize# #adjective.capitalize#'],
    'title': '#setTitleType# #roomName.capitalize#',
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

rooms = []
for i in range(50):
    rooms.append(grammar.flatten('#title#'))

print(rooms)