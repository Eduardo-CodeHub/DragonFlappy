import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH


class Final:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/FinalBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def flevel(self, menu_return):
        pygame.mixer_music.load('./asset/FinalBg.mp3')
        pygame.mixer_music.play()
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.final_text(48, '!!YOU ARE THE WINNER!!', (255, 255, 0), (WIN_WIDTH / 2, 50))
            self.final_text(25, '!CONGRATULATIONS!', (255, 255, 255), (WIN_WIDTH / 2, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            pass

    def final_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
