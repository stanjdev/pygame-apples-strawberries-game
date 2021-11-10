import pygame
pygame.init()
from random import randint, choice

clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
w, h = pygame.display.get_surface().get_size()


# surf = pygame.Surface((50, 50))
# surf.fill((255, 111, 33))


class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height))
    # self.surf.fill((255, 0, 255))
    self.surf = pygame.image.load(image)
    self.rect = self.surf.get_rect()
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect()
  
  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))

# instance of GameObject 
# box = GameObject(120, 300, 50, 50)
# apple = GameObject(0, 250, './images/apple.png')
# strawberry = GameObject(250, 250, './images/strawberry.png')

apple2 = GameObject(w / 2, 0, './images/apple.png')


# 3 LANES FOR VERTICAL AND HORIZONTAL
center = w / 2
middle = center - 32
left = center / 2 - 25
right =  w - (center / 2) - 25

x_lanes = [left, middle, right]

center_horizontal = h / 2
center_horizontal_lane = center_horizontal - 32
top = center_horizontal / 2 - 25
bottom = h - (center_horizontal / 2) - 25

y_lanes = [top, center_horizontal_lane, bottom]


class Apple(GameObject):
  def __init__(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    super(Apple, self).__init__(0, 0, './images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > h:
      self.reset()

  def reset(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    self.y = -64


class Strawberry(GameObject):
  def __init__(self):
    # self.y = randint(50, 400)
    self.y = choice(y_lanes)
    super(Strawberry, self).__init__(0, 0, './images/strawberry.png')
    self.dy = 0
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.x > w:
      self.reset()
  
  def reset(self):
    self.y = choice(y_lanes)
    # self.y = randint(50, 400)
    self.x = -64

apple = Apple()
strawberry = Strawberry()


# PLAYER CLASS
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, './images/player.png')
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


player = Player()


# Make a group
all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)








# GAME LOOP

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
      

  fill_color = (255, 255, 255)
  # Clear screen
  screen.fill(fill_color)
  # screen.blit(surf, (100, 100))
  # box.render(screen)

  # apple.move()
  # apple.render(screen)
  # apple2.render(screen)

  # strawberry.move()
  # strawberry.render(screen)
  
  # # Draw player
  # player.move()
  # player.render(screen)

  for entity in all_sprites:
    entity.move()
    entity.render(screen)


  # Update the window
  pygame.display.flip()
  # tick the clock
  clock.tick(60)

