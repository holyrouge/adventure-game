from .models import *
import random


class AdventureGame:
  def __init__(self, max_x=5, max_y=5):
    self.num_turns = 1
    self.max_x = max_x
    self.max_y = max_y
    self.world = [[WorldPiece(x, y) for x in range(self.max_x)] for y in range(self.max_y)]
    self.terrain_types = {"grass": "W", "mountain": "^", "plains": " "}
    pass

  def play(self):
    self.world = [[Land(x, y, hidden=False) for x in range(self.max_x)] for y in range(self.max_y)]
    for y in range(self.max_y):
      for x in range(self.max_x):
        terrain = random.choice(list(self.terrain_types.keys()))
        terrain_symbol = self.terrain_types[terrain]
        self.world[y][x].terrain = terrain
        self.world[y][x].symbol = terrain_symbol

    print("Adventure Game")

    player_first_name = input("Adventurer's First Name: ")
    player_last_name = input("Adventurer's Last Name: ")

    player = Adventurer(x=0, y=0, land=self.world[0][0], first_name=player_first_name,
                        last_name=player_last_name)
    # world[y][x]
    self.world[0][0] = player

    print("Player named " + player.first_name + " " + player.last_name + " created.")
    print("Game Instructions:")
    print("Move the Adventurer in the appropriate directions by entering W, A, S, or D.")
    print("Enter X to exit.")
    print("Let's Start!")

    while True:
      self.turn()

      user_cmd = input("Enter W, A, S, or D to move, X to exit: ")
      user_cmd = user_cmd.upper()

      if user_cmd == "W":
        if player.y != 0:
          self.world[player.y][player.x] = player.land
          player.y -= 1
          player.land = self.world[player.y][player.x]
          self.world[player.y][player.x] = player
        else:
          print("The Adventurer can't move that away any more. Please try again.")
          continue
      elif user_cmd == "A":
        if player.x != 0:
          self.world[player.y][player.x] = player.land
          player.x -= 1
          player.land = self.world[player.y][player.x]
          self.world[player.y][player.x] = player
        else:
          print("The Adventurer can't move that away any more. Please try again.")
          continue
      elif user_cmd == "S":
        if player.y != (self.max_y - 1):
          self.world[player.y][player.x] = player.land
          player.y += 1
          player.land = self.world[player.y][player.x]
          self.world[player.y][player.x] = player
        else:
          print("The Adventurer can't move that away any more. Please try again.")
          continue
      elif user_cmd == "D":
        if player.x != (self.max_x - 1):
          self.world[player.y][player.x] = player.land
          player.x += 1
          player.land = self.world[player.y][player.x]
          self.world[player.y][player.x] = player
        else:
          print("The Adventurer can't move that away any more. Please try again.")
          continue
      elif user_cmd == "X":
        break
      else:
        print("Incorrect command. Please try again.")
        continue

      self.num_turns += 1

    self.exit()

  def turn(self):
    print("Turns: " + str(self.num_turns))
    print("Current Board: ")
    self.display_game()

  def exit(self):
    print("--------------------")
    print("The game has ended.")
    print("The number of turns played: " + str(self.num_turns))
    self.display_game()

  def display_game(self):
    print("___" * self.max_x)
    for y in range(self.max_y):
      row = "|"
      for x in range(self.max_x):
        row += self.world[y][x].symbol + "  "
      print(row[0:len(row) - 2] + "|")
    print("---" * self.max_x)
