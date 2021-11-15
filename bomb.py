from game_object import GameObject
from random import randint, choice
from constants import x_lanes, SCREEN_HEIGHT

# BOMB CLASS
class Bomb(GameObject):
  def __init__(self):
    self.x = choice(x_lanes)
    super(Bomb, self).__init__(0, 0, './images/bomb.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > SCREEN_HEIGHT:
      self.reset()

  def reset(self):
    self.x = choice(x_lanes)
    self.y = -64

