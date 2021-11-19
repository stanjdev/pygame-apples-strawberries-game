from animated_object import AnimatedObject
from constants import x_lanes, y_lanes

import pygame

pink_images = [
  pygame.image.load('./images/pink/pink-1.gif'),
  pygame.image.load('./images/pink/pink-2.gif'),
  pygame.image.load('./images/pink/pink-3.gif'),
  pygame.image.load('./images/pink/pink-4.gif'),
  pygame.image.load('./images/pink/pink-5.gif'),
  pygame.image.load('./images/pink/pink-6.gif'),
  pygame.image.load('./images/pink/pink-7.gif'),
  pygame.image.load('./images/pink/pink-8.gif'),
  pygame.image.load('./images/pink/pink-9.gif'),
  pygame.image.load('./images/pink/pink-10.gif'),
  pygame.image.load('./images/pink/pink-11.gif'),
]

# AnimatedPlayer CLASS
class AnimatedPlayer(AnimatedObject):
  def __init__(self):
    super(AnimatedPlayer, self).__init__(0, 0, files=pink_images)
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(x_lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self): 
    if self.pos_y < len(y_lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = x_lanes[self.pos_x]
    self.y = y_lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y

  def update_dx_dy(self):
    self.dx = x_lanes[self.pos_x]
    self.dy = y_lanes[self.pos_y]


