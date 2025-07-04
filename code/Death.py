import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT


class DeathScreen:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/DeathBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        try:
            pygame.mixer_music.load('./asset/DeathBg.mp3')
            pygame.mixer_music.play()
        except pygame.error:
            print('')

        # Draw the screen
        self.window.blit(source=self.surf, dest=self.rect)
        self.draw_text(60, 'YOU DIED', (180, 0, 0), (WIN_WIDTH / 2, WIN_HEIGHT / 2.5))
        self.draw_text(20, 'Better luck next time...', (255, 255, 255), (WIN_WIDTH / 2, WIN_HEIGHT / 1.8))

        pygame.display.flip()
        # Pause the game for 4 seconds
        pygame.time.wait(4000)

    def draw_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
