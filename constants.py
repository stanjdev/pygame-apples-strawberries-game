import pygame
pygame.init()
pygame.font.init()

# Configure the Screen
screen = pygame.display.set_mode([500, 500]) # SQUARE
# screen = pygame.display.set_mode([375, 667]) # MOBILE App
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

# BACKGROUND IMAGE
bg_image = pygame.image.load('./images/fruits.gif').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

gamefont = pygame.font.SysFont('Comic Sans MS', 30)

# CONSTANTS
# 3 LANES FOR VERTICAL AND HORIZONTAL - in case canvas size is uneven
center = SCREEN_WIDTH / 2
middle = center - 32
left = center / 2 - 25
right =  SCREEN_WIDTH - (center / 2) - 25
x_lanes = [left, middle, right]

center_horizontal = SCREEN_HEIGHT / 2
center_horizontal_lane = center_horizontal - 32
top = center_horizontal / 2 - 25
bottom = SCREEN_HEIGHT - (center_horizontal / 2) - 25
y_lanes = [top, center_horizontal_lane, bottom]

speed_increase_value = 0.1

