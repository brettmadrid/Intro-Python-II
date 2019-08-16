# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room, inventory):
      self.name = name
      self.current_room = current_room
      self.inventory = inventory

  def __str__(self):
      # return f'{self.name}, you are in the {self.current_room} room'
      return "Name: {}, Room: {}, Items in inventory: {}".format(self.name, self.current_room, self.inventory)

  def action_input(self, decision):
    bad_choice = '\n*** There is no room here to go to, make another choice ***\n'
    if decision == 'n':
      if self.current_room.n_to is not None:
          self.current_room = self.current_room.n_to
      else:
        print(bad_choice)
    elif decision == 's':
      if self.current_room.s_to is not None:
        self.current_room = self.current_room.s_to
      else:
        print(bad_choice)
    elif decision == 'e':
      if self.current_room.e_to is not None:
        self.current_room = self.current_room.e_to
      else:
        print(bad_choice)
    elif decision == 'w':
      if self.current_room.w_to is not None:
        self.current_room = self.current_room.w_to
      else:
        print(bad_choice)
    elif decision == 'l':
        self.look_around()
    elif decision == 'i':
        self.take_inventory()
    elif decision == 'r':
      self.remove_item()
    elif decision == 'q':
      pass
    else:
      print("Sorry, that is not a valid choice!")

  def describe_room(self):
    print(f'\n\nYour location: {self.current_room.name}\n \n{self.current_room.description}\n')

  def look_around(self):
    if self.current_room.items:
            pick_up = input(f"You see a ({self.current_room.items.name}), pick it up? (y/n)")
            if pick_up == 'y':
              self.inventory.append(self.current_room.items)
              print(f'\n{self.current_room.items.name} added to your inventory\n')
            else:
              print('\n\nYou continue to move through the room')
            
    else:
      print("\n\nNothing of interest here.  A few rats scurry away as you move on.")

  def take_inventory(self):
    if self.inventory:
      print('You have:\n')
      for i in self.inventory:
        print(i.name)
    else:
      print('You currently have no items!')

  def remove_item(self):
    if self.inventory:
      remove = input("\n\nWhich item would you like to remove? ")

      for i in self.inventory:
        print(i)
        # if item.name == remove:
        #   del self.inventory[i]
        #   print('Item successfully removed\n')
        #   self.take_inventory()
    else:
      print('You currently have no items!')

    
