from game_object import GameObject
from random import randint, choice
from constants import x_lanes, speed_increase_value, SCREEN_HEIGHT

# APPLE CLASS
class Apple(GameObject):
  def __init__(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    super(Apple, self).__init__(0, 0, './images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def increase_speed(self):
    self.dy += speed_increase_value

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > SCREEN_HEIGHT:
      self.reset()

  def reset(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    self.y = -64
    
  def reset_speed(self):
    self.dy = (randint(0, 200) / 100) + 1

