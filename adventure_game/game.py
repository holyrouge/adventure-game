from .models import *

class AdventureGame:
  def __init__(self, max_x=5, max_y=5):
    self.num_turns = 0
    self.max_x = max_x
    self.max_y = max_y
    self.world = [[WorldPiece(x, y) for x in range(self.max_x)] for y in range(self.max_y)]
    self.world[0][0] = Adventurer()
    pass

  def play(self):
    pass

  def display_game(self):
    print("Current Board: ")
    print("Turns: " + str(self.num_turns))
    print("___" * self.max_x)
    for y in range(self.max_y):
      row = "|"
      for x in range(self.max_x):
        row += self.world[y][x].symbol + "  "
      print(row[0:len(row)-2] + "|")
    print("---" * self.max_x)

  def exit(self):
    pass