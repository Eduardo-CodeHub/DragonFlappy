from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'Null'

    @abstractmethod
    def move(self, ):
        pass
