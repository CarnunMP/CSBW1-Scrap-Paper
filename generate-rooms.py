import tracery
from tracery.modifiers import base_english

basicRoomFeatures = 'panels,lights,exposed wires'

rules = {
    'setRoomName': [
        f'[roomName:room][features:{basicRoomFeatures}]',
        f'[roomName:corridor][features:{basicRoomFeatures}]', 
        f'[roomName:medbay][features:{basicRoomFeatures},medical supplies,empty beds]'
    ],
    # 'roomName': ['room', 'corridor', 'medbay', 'armoury', 'quarters', 'bridge', 'brig', 'passageway', 'laboratory', 'mess-hall', 'engine-room'],
    'adjective': ['dark', 'smoky', 'dangerous-looking', 'messy', 'quiet', 'irradiated', 'full', 'empty', 'packed', 'stripped', 'ransacked'],
    'adverb': ['suspiciously', 'strangely', 'worryingly', 'puzzlingly', 'suprisingly', 'curiously'],
    'setTitleType': ['#adjective.capitalize#', '#adverb.capitalize# #adjective.capitalize#'],
    'title': '#setTitleType# #roomName.capitalize#',

    'description': 'You see some #features#.',

    'origin': '#[#setRoomName#]title#: #description#'
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

rooms = []
for i in range(50):
    rooms.append(grammar.flatten('#origin#'))

print(rooms)