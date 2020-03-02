import tracery
from tracery.modifiers import base_english

basicRoomFeatures = 'panel,light,cable'

rules = {
    'setRoomName': [
        f'[roomName:room][feature:{basicRoomFeatures}]',
        f'[roomName:corridor][feature:{basicRoomFeatures}]', 
        f'[roomName:medbay][feature:{basicRoomFeatures},medkit,empty bed]',
        f'[roomName:armoury][feature:{basicRoomFeatures},phaser,pistol,assault rifle,grenade,odd-looking gun]',
        f'[roomName:quarters][feature:{basicRoomFeatures},mirror,jewel,family photo,picture of a dog]',
        f'[roomName:bridge][feature:{basicRoomFeatures},chair,flight computer]',
        f'[roomName:brig][feature:{basicRoomFeatures},force field,handcuff]',
        f'[roomName:passageway][feature:{basicRoomFeatures},communicator]',
        f'[roomName:laboratory][feature:{basicRoomFeatures},test tube,centrifuge,lazer]',
        f'[roomName:mess-hall][feature:{basicRoomFeatures},pot,pan,vegetable,fruit,plate,knife,fork,replicator]',
        f'[roomName:engine-room][feature:{basicRoomFeatures},pipe,reactor,green gelatinous puddle]',
    ],
    'adjective': ['dark', 'smoky', 'dangerous-looking', 'messy', 'quiet', 'irradiated', 'full', 'empty', 'packed', 'stripped', 'ransacked'],
    'adverb': ['suspiciously', 'strangely', 'worryingly', 'puzzlingly', 'suprisingly', 'curiously'],
    'setTitleType': ['#adjective.capitalize#', '#adverb.capitalize# #adjective.capitalize#'],
    'title': '#setTitleType# #roomName.capitalize#',

    'description': [
        'You see #feature.a#.',
        'You bend over, and spot several #feature.s#.'
    ],

    'origin': '#[#setRoomName#]title#: #description#'
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

rooms = []
for i in range(50):
    rooms.append(grammar.flatten('#origin#'))

print(rooms)