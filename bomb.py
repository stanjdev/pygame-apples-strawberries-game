from game_object import GameObject
from random import randint, choice
from constants import x_lanes, y_lanes, SCREEN_HEIGHT, SCREEN_WIDTH

# BOMB CLASS
class Bomb(GameObject):
  def __init__(self):
    self.x = choice(x_lanes)
    super(Bomb, self).__init__(0, 0, './images/bomb.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.direction = choice(['toBottom', 'toTop', 'toRight', 'toLeft'])
    self.reset()

  def move(self):
    self.x += self.dx if self.direction == 'toBottom' or self.direction == 'toTop' else self.dy if self.direction == 'toRight' else -abs(self.dy) if self.direction == 'toLeft' else self.dx
    self.y += self.dy if self.direction == 'toBottom' else -abs(self.dy) if self.direction == 'toTop' else 0
    if self.y > SCREEN_HEIGHT or self.y < -64 or self.x > SCREEN_WIDTH or self.x < -64:
      self.reset()

  def reset(self):
    self.direction = choice(['toBottom', 'toTop', 'toRight', 'toLeft'])
    self.x = choice(x_lanes) if self.direction == 'toBottom' or self.direction == 'toTop' else -64 if self.direction == 'toRight' else SCREEN_WIDTH if self.direction == 'toLeft' else choice(x_lanes)
    self.y = -64 if self.direction == 'toBottom' else SCREEN_HEIGHT if self.direction == 'toTop' else choice(y_lanes)
    # print("Bomb moving: " + self.direction)

