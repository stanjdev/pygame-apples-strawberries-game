import pygame

pink_images = [
  './images/pink/pink-1.png'
  './images/pink/pink-2.png'
  './images/pink/pink-3.png'
  './images/pink/pink-4.png'
  './images/pink/pink-5.png'
]

class AnimatedObject(pygame.sprite.Sprite):
  def __init__(self, x, y, files):
    super(AnimatedObject, self).__init__()
    self.x = x
    self.y = y
    self.images = []
    self.index = 0

    for image in files:
      print(image)
      # self.surf = pygame.image.load(image)
      self.images.append(self.surf)
      self.rect = self.surf.get_rect()
    # Create a surface from each file in files and add a surface to the images list

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    self.index += 1
    if (self.index >= len(self.images)):
      self.index = 0
    for surface in self.images:
      screen.blit(surface, (self.x, self.y))
    # increment index
    # if index is equal to the length of the images
    # set index to 0 for it to loop
    # blit the surface in images at the index to the screen


animated_player = AnimatedObject(0, 0, pink_images)

