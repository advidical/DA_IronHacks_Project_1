#DEFINE ROOMS
# define rooms and items

# Doors:
door_a = {
    "name": "door a",
    "type": "door",
}
door_b = {
    "name": "door b",
    "type": "door",
}
door_c = {
    "name": "door c",
    "type": "door",
}
door_d = {
    "name": "door d",
    "type": "door",
}

#Game Room
couch = {
    "name": "couch",
    "type": "furniture",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

#Bedroom 1

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}


key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}


bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

#Bedroom 2
double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}


key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

#Living Room

dining_table = {
    "name": "dining table",
    "type": "furniture",
}


living_room = {
    "name": "living room",
    "type": "room",
}

#Outside
outside = {
  "name": "outside"
}

# Unused
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]
all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related
INIT_OBJECT_RELATIONS = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "bedroom 1": [queen_bed, door_a,door_b,door_c],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "door b": [bedroom_1, bedroom_2],
    "door c": [living_room, bedroom_1],
    "door d": [living_room, outside],
    "bedroom 2": [double_bed,dresser,door_b],
    "living room": [dining_table, door_c, door_d],
}
# Define Game State
INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}