import pygame

# GAME OBJECT
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height))
    # self.surf.fill((255, 0, 255))
    self.surf = pygame.image.load(image)
    self.rect = self.surf.get_rect()
    self.x = x
    self.y = y
  
  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))

# instance of GameObject 
# box = GameObject(120, 300, 50, 50)
# apple = GameObject(0, 250, './images/apple.png')
# strawberry = GameObject(250, 250, './images/strawberry.png')
