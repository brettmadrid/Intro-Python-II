# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
      self.name = name
      self.current_room = current_room

  def __str__(self):
      # return str(self.__dict__)
      # return f'{self.name}, you are in the {self.current_room} room'
      return "Name: {}, Room: {}".format(self.name, self.current_room)

  def action_input(self, decision):
    if decision == 'n':
      if self.current_room.n_to is not None:
          self.current_room = self.current_room.n_to
          print('Your are in the foyer')
    elif decision == 's':
      if self.current_room.s_to is not None:
        self.current_room = self.current_room.s_to
    elif decision == 'e':
      if self.current_room.e_to is not None:
        self.current_room = self.current_room.e_to
    elif decision == 'w':
      if self.current_room.w_to is not None:
        self.current_room = self.current_room.w_to
    else:
      print("Thanks for playing")

