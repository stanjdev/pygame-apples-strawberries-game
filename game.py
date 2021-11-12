# https://github.com/Tech-at-DU/Pygame-Tutorial 

import pygame
pygame.init()
from random import randint, choice
from game_object import GameObject

clock = pygame.time.Clock()

# Configure the screen
# screen = pygame.display.set_mode([375, 667]) # Mobile App
screen = pygame.display.set_mode([500, 500]) # Square
w, h = pygame.display.get_surface().get_size()

bg_image = pygame.image.load('./images/fruits.gif')
bg_image = pygame.transform.scale(bg_image, (w, h))

# surf = pygame.Surface((50, 50))
# surf.fill((255, 111, 33))



apple2 = GameObject(w / 2, 0, './images/apple.png')


# 3 LANES FOR VERTICAL AND HORIZONTAL - in case canvas size is uneven
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

speed_increase_value = 0.1

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
    if self.y > h:
      self.reset()

  def reset(self):
    # self.x = randint(50, 400)
    self.x = choice(x_lanes)
    self.y = -64
    self.increase_speed()


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
    if self.x > w:
      self.reset()
  
  def reset(self):
    self.y = choice(y_lanes)
    # self.y = randint(50, 400)
    self.x = -64
    self.increase_speed()

apple = Apple()
strawberry = Strawberry()



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
    if self.y > h:
      self.reset()

  def reset(self):
    self.x = choice(x_lanes)
    self.y = -64

# Vertical top to bottom
bomb = Bomb()




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



# Make a Group to render and move all sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)


# Make a fruits Group
fruits_sprites = pygame.sprite.Group()

fruits_sprites.add(apple)
fruits_sprites.add(strawberry)


# RESET ENTIRE GAME
def initialize_game():
  # RESET THE SPEEDS FOR EACH ITEM too.
  player.reset()
  # RESET THE PLAYER'S POSITION
  apple.reset()
  strawberry.reset()
  bomb.reset()






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
  screen.blit(bg_image, (0, 0))
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


  # Returns the fruit that the player has collided with
  fruit = pygame.sprite.spritecollideany(player, fruits_sprites)
  if fruit:
    print(fruit)
    fruit.reset()
    

  # # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    # running = False
    initialize_game()

    # RESET FRUITS, BOMBS, AND PLAYER positions


  # Update the window
  pygame.display.flip()
  # tick the clock
  clock.tick(60)

