import pygame
from settings import WIDTH, HEIGHT
from pathlib import Path
from PIL import Image


class AssetsManager:
    def __init__(self):
        pygame.mixer.init()

        # Imagenes y fuentes
        self.assets_path = Path(__file__).resolve().parents[1] / "assets"
        self.font_path = self.assets_path / "pixel_font.ttf"
        self.bg_path = self.assets_path / "background.jpeg"

        # Sonidos
        self.intro_sound = pygame.mixer.Sound(str(self.assets_path / "Intro.wav"))
        self.background_music = pygame.mixer.Sound(
            str(self.assets_path / "background.mp3")
        )
        self.score_sound = pygame.mixer.Sound(str(self.assets_path / "points.wav"))
        self.bounce_sound = pygame.mixer.Sound(str(self.assets_path / "pong.wav"))
        self.game_over_sound = pygame.mixer.Sound(
            str(self.assets_path / "game_over.wav")
        )

    def get_font(self, size):
        return pygame.font.Font(str(self.font_path), size)

    def get_bg_img(self):
        image = Image.open(self.bg_path).convert("RGB")
        background = pygame.image.fromstring(image.tobytes(), image.size, "RGB")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        return background
