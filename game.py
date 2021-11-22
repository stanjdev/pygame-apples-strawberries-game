# https://github.com/Tech-at-DU/Pygame-Tutorial 

import pygame
pygame.init()
pygame.font.init()
# from player import Player
# from bomb import Bomb
from strawberry import Strawberry
from apple import Apple
from constants import screen, bg_image, gamefont

from player_animated import AnimatedPlayer
from bomb_animated import AnimatedBomb

clock = pygame.time.Clock()

# Apples move vertically
apple = Apple()

# Strawberries move horizontally
strawberry = Strawberry()

# BOMB INSTANCE
# bomb = Bomb()
bomb = AnimatedBomb()

# PLAYER INSTANCE
# player = Player()
player = AnimatedPlayer()


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

score = 0


# RESET ENTIRE GAME WHEN TOUCHING A BOMB
def initialize_game():
  player.reset()
  # RESET THE PLAYER'S POSITION
  bomb.reset()
  for fruit in fruits_sprites:
    fruit.reset_speed()
    fruit.reset()



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
        
  # Set background image
  screen.blit(bg_image, (0, 0))

  # Score counter
  score_surface = gamefont.render(f"Score: {score}", False, (0, 0, 0))
  screen.blit(score_surface, (0, 0))

  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  # # Returns the fruit that the player has collided with
  fruit = pygame.sprite.spritecollideany(player, fruits_sprites)
  if fruit:
    fruit.increase_speed()
    fruit.reset()
    score += 1

  # # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    # running = False
    score = 0
    initialize_game()


  # Update the window
  pygame.display.flip()
  # tick the clock
  clock.tick(60)





