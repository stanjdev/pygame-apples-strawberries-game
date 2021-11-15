from game_object import GameObject
from random import randint, choice
from constants import y_lanes, speed_increase_value, SCREEN_WIDTH

# STRAWBERRY CLASS
class Strawberry(GameObject):
  def __init__(self):
    # self.y = randint(50, 400)
    self.y = choice(y_lanes)
    super(Strawberry, self).__init__(0, 0, './images/strawberry.png')
    self.dy = 0
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()

  def increase_speed(self):
    self.dx += speed_increase_value

  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.x > SCREEN_WIDTH:
      self.reset()
  
  def reset(self):
    self.y = choice(y_lanes)
    # self.y = randint(50, 400)
    self.x = -64

  def reset_speed(self):
    self.dx = (randint(0, 200) / 100) + 1
    