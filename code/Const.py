# M
import pygame

MENU_OPTION = ('NEW GAME',
               'GAME TIME',
               'EXIT')

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Player1': 3,
    'Enemy1': 1,
    'Enemy2': 2
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1': 1,
    'Enemy1': 100,
    'Enemy2': 100,
}

# S
SPAWN_TIME = 3000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
