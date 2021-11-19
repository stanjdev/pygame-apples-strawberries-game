import pygame

class AnimatedObject(pygame.sprite.Sprite):
  def __init__(self, x, y, files):
    super(AnimatedObject, self).__init__()
    self.x = x
    self.y = y
    self.images = files
    self.index = 0
    self.surf = self.images[0]

  def render(self, screen):
    self.rect = self.surf.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    self.surf = self.images[self.index]
    self.index += 1
    if (self.index >= len(self.images)):
      self.index = 0
    screen.blit(self.surf, (self.x, self.y))




