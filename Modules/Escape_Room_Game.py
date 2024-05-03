# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

from Escape_Room_Data import *

game_state = INIT_GAME_STATE.copy()
object_relations = INIT_OBJECT_RELATIONS.copy()

def linebreak():
    """
    Print a line break
    """
    print("-"*80+"\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with"+
          "\nno windows which you have never been to before." +
          "\nYou don't remember why you are here and what had happened before. " +
          "\nYou feel some unknown danger is approaching and "+
          "\nyou must get out of the house, NOW!")
    linebreak()
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    while (game_state["current_room"] != game_state["target_room"]):
      room = game_state["current_room"]
      print("You are now in " + room["name"])
      intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip().lower()
      if intended_action == "explore":
          explore_room(room)
      elif intended_action == "examine":
          search = input("What would you like to examine?").strip().lower()
          # examine your search: if we find something, return the corresponding object
          found = examine_item(search)
          if found == None:
            print("The item you requested is not found in the current room.")
            continue
          print(f"You examine {found['name']}.")
          # found door
          if found['type'] == "door" and check_door(found):
            # call function to see if you can open it with key_inventory
            game_state["current_room"] = enter_room(found,game_state["current_room"])
          elif found['type'] == 'furniture':
            #type of furniture - call function to search for a key
            check_furniture(found)
          else: # Note: will never be called with baseline game
            print("Don't know what THAT is, but you can't interact with it.")

      else:
          print("Not sure what you mean. Type 'explore' or 'examine'.")
      linebreak()

      if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
        return

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def check_furniture(item):
  """checks if furniture has a key to find
     Returns: True of False depending if we find a key
  """
  if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
      key = object_relations[item["name"]].pop()
      game_state["keys_collected"].append(key)
      print(f"You search the {item['name']} and find a key: {key['name']}.")
      return True
  print("There isn't anything interesting about it.")
  return False

def get_next_room_of_door(door, current_room): # Only function from old version to be used in our code
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def enter_room(door,current_room):
  """
  Helper function for check door:
  Prompt User if they want to open the door and enter the next room
  Returns : a room
  """
  decision = ''
  next_room = current_room
  while decision not in set(['yes','no']):
    decision = input(f"Do you want to open {door['name']} and enter the next room? (yes/no): ").lower()
    if decision == "yes":
      next_room = get_next_room_of_door(door, current_room)
      print(f"You open {door['name']} and enter {next_room['name']}.")
    elif decision == "no":
      print(f"You decide not to open {door['name']} and stay in {current_room['name']}.")
    else:
      print("Please enter 'yes' or 'no'.")

  return next_room

def check_door(door):
  """ Checks if door can be opened: return True or False"""
  for key in game_state["keys_collected"]:
      if(key["target"] == door):
          print(f"We have {key['name']}! We can unlock {door['name']}")
          return True
  print(f"We don't have the key to unlock {door['name']}")
  return False

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First check to see if the item exists: if it doesn't, return None
    Else return the found object.
    """
    current_room = game_state["current_room"]
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
          return item

if __name__ == "__main__":
  start_game()