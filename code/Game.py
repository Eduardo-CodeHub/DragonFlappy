#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Final import Final
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            final = Final(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1Bg', menu_return)
                level_return = level.run()
                if level_return:
                    level = Level(self.window, 'Level2Bg', menu_return)
                    level_return = level.run()
                    if level_return:
                        level = Level(self.window, 'Level3Bg', menu_return)
                        level_return = level.run()
                        if level_return:
                            final.flevel(menu_return)

            elif menu_return == MENU_OPTION[1]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
