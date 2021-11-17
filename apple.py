from game_object import GameObject
from random import randint, choice
from constants import SCREEN_WIDTH, x_lanes, speed_increase_value, SCREEN_HEIGHT

# APPLE CLASS
class Apple(GameObject):
  def __init__(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    super(Apple, self).__init__(0, 0, './images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.direction = choice(['toBottom', 'toTop'])
    self.reset()

  def increase_speed(self):
    self.dy += speed_increase_value

  def move(self):
    self.x += self.dx
    self.y += self.dy if self.direction == 'toBottom' else -abs(self.dy)
    if self.y > SCREEN_HEIGHT or self.y < -64:
      self.reset()

  def reset(self):
    self.direction = choice(['toBottom', 'toTop'])
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    self.y = -64 if self.direction == 'toBottom' else SCREEN_HEIGHT
    
  def reset_speed(self):
    self.dy = (randint(0, 200) / 100) + 1

