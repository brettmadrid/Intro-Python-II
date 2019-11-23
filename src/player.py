# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'Name: {self.name}, Room: {self.current_room}'

    def action_input(self, decision):
        bad_choice = "\n***Not an option! Make another choice.***\n"

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
