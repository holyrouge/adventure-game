class WorldPiece:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.symbol = " "


class Land(WorldPiece):
  def __init__(self, x=0, y=0, hidden=True, terrain="empty", symbol="L"):
    super(Land, self).__init__(x, y)
    self.hidden = hidden
    self.terrain = terrain
    self.symbol = symbol

  def reveal(self):
    pass


class Person(WorldPiece):
  def __init__(self, x=0, y=0, land=Land(0, 0, False, "empty"), first_name="Adventurer", last_name="Person"):
    super(Person, self).__init__(x, y)
    self.first_name = first_name
    self.last_name = last_name
    self.land = land
    self.symbol = "O"


class Adventurer(Person):
  def __init__(self, x=0, y=0, land=Land(0, 0, False, "empty"), first_name="Adventurer", last_name="Person"):
    super(Adventurer, self).__init__(x, y, land, first_name, last_name)
    self.symbol = "A"

  def move(self, num_steps=0, direction=None):
    pass

  def explore(self, direction=None):
    pass

