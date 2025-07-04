import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Death import DeathScreen
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

                # Level 1
                level1 = Level(self.window, 'Level1Bg', menu_return)
                level_return = level1.run()
                if level_return == "DIED":
                    death_screen = DeathScreen(self.window)
                    death_screen.run()
                    continue  # Back to menu

                # Level 2 (if Level 1 is True)
                if level_return is True:
                    level2 = Level(self.window, 'Level2Bg', menu_return)
                    level_return = level2.run()
                    if level_return == "DIED":
                        death_screen = DeathScreen(self.window)
                        death_screen.run()
                        continue

                # Level 3
                if level_return is True:
                    level3 = Level(self.window, 'Level3Bg', menu_return)
                    level_return = level3.run()
                    if level_return == "DIED":
                        death_screen = DeathScreen(self.window)
                        death_screen.run()
                        continue

                # End screen
                if level_return is True:
                    final = Final(self.window)
                    final.flevel(menu_return)

            elif menu_return == MENU_OPTION[1]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
