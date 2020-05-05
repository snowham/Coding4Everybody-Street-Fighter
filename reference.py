import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (102, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BRIGHT_RED = (170, 1, 20)
DARK_RED = (128, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)
BROWN = (150, 75, 0)

# basic constants to set up your game
WIDTH = 750 #original WIDTH: 750
HEIGHT = 580 #original HEIGHT: 580
FPS = 30
BGCOLOR = BLACK
WINDOW_TITLE = "Coding4Everybody - Street Fighter"

GROUND_LEVEL = 320 #original GROUND_LEVEL: 268

PUNCH_DAMAGE = 10
PUNCH_COOLDOWN = 5
PUNCH_DURATION = 5

JUMP_STRENGTH = 50 #shouldn't be related to height
GRAVITY = 6

FIGHTER_HITBOX_X1 = 10
FIGHTER_HITBOX_Y1 = 0
FIGHTER_HITBOX_X2 = 90
FIGHTER_HITBOX_Y2 = 160
DRAW_HITBOXES = False

HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_AMPLIFIER = 3
HEALTH_BAR_BORDER_WIDTH = 5
HEALTH_BAR_OLD_HEALTH_DELAY = 20
HEALTH_BAR_OLD_HEALTH_DECREASE_SPEED = 3
HEALTH_BAR_PLAYER_1_START_X = 20
HEALTH_BAR_PLAYER_1_START_Y = 25
HEALTH_BAR_PLAYER_2_START_X = 345
HEALTH_BAR_PLAYER_2_START_Y = 20


F1_RIGHT = pygame.transform.scale(pygame.image.load(
    '/home/runner/Coding4Everybody-Street-Fighter/positions/fighter1_right.png'), (106, 157))

F1_LEFT = pygame.transform.scale(pygame.image.load(
    '/home/runner/Coding4Everybody-Street-Fighter/positions/fighter1_left.png'), (106, 157))

L1_PUNCH = pygame.transform.scale(pygame.image.load(
    "/home/runner/Coding4Everybody-Street-Fighter/positions/punch1_left.png"), (133, 154))

R1_PUNCH = pygame.transform.scale(pygame.image.load(
    "/home/runner/Coding4Everybody-Street-Fighter/positions/punch1_right.png"), (133, 154))

F2_RIGHT = pygame.transform.scale(pygame.image.load(
    '/home/runner/Coding4Everybody-Street-Fighter/positions/fighter2_right.png'), (106, 157))

F2_LEFT = pygame.transform.scale(pygame.image.load(
    '/home/runner/Coding4Everybody-Street-Fighter/positions/fighter2_left.png'), (106, 157))

L2_PUNCH = pygame.transform.scale(pygame.image.load(
    "/home/runner/Coding4Everybody-Street-Fighter/positions/punch2_left.png"), (133, 154))

R2_PUNCH = pygame.transform.scale(pygame.image.load(
    "/home/runner/Coding4Everybody-Street-Fighter/positions/punch2_right.png"), (133, 154))

BACKGROUND = pygame.transform.scale(pygame.image.load(
    "/home/runner/Coding4Everybody-Street-Fighter/positions/background.gif"), (WIDTH, HEIGHT))


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def quit_game():
    pygame.quit()
    quit()

def button(screen,msg,x,y,width,height,inactiveColor,activeColor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, activeColor,(x,y,width,height))

        if click[0] == 1 and action != None:
            action(screen)         
    else:
        pygame.draw.rect(screen, inactiveColor,(x,y,width,height))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(width/2)), (y+(height/2)))  
    screen.blit(textSurf, textRect)