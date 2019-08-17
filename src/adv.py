from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of money permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! There is so much treasure here that you will have to make several trips."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# create items
item = {
    'rock':  Item("Rock",
                     "a large palm sized rock lies at your feet"),
    'gun':   Item("Gun",
                    "a 9mm Glock pistol"),
    'painting': Item("Painting",
                    "a long lost Picasso painting on the wall"),
}   

# put items in rooms
room['outside'].items = item['rock']
room['foyer'].items = item['painting']
room['narrow'].items = item['gun']


# Make a new player object that is currently in the 'outside' room.
player = Player(input("Ready Player One! Enter your name please: "), room['outside'], [])

action = input("\n\nYou are standing outside facing the mouth of a well concealed cave you may try to: Move North(n), South(s), East(e), or West(w), Look Around(l)\nTake Inventory(i)\nRemove Item(r)\n,or you can quit the game(q)\n\n")

player.action_input(action)
# Write a loop that:
while True:
    if action == 'q':
        break
    elif player.current_room is not None:
        player.describe_room() 
        action = input("What would you like to do?\n\nMove North(n)\nMove South(s)\nMove East(e)\nMove West(w)\nLook Around(l)\nTake Inventory(i)\nRemove Item(r)\nQuit Game(q)\n")
        player.action_input(action)
        continue
    else:
        print("Room does not exist. Please try again.")

