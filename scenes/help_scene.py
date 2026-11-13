import pygame
from settings import (
    WIDTH,
    HEIGHT,
    BACKGROUND_COLOR,
    FILL_COLOR,
    FILL_COLOR_HOVERED,
    HEADING_COLOR,
    BORDER_COLOR,
    BORDER_COLOR_HOVERED,
    TEXT_COLOR,
    TEXT_COLOR_HOVERED,
    WIN_INFO_COLOR,
    TITLE_TEXT_COLOR,
)


class HelpScene:
    def __init__(self, assets):
        self.assets = assets
        self.title_font = self.assets.get_font(80)
        self.subtitle_font = self.assets.get_font(36)
        self.text_font = self.assets.get_font(26)
        self.back_btn = pygame.Rect(0, 0, 240, 55)
        self.back_btn.center = (WIDTH // 2, HEIGHT - 100)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render("= HELP =", True, TITLE_TEXT_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 65)))

        heading_color = HEADING_COLOR
        text_color = TEXT_COLOR

        lines = [
            ("PLAYER 1", heading_color),
            ("W - Move up", text_color),
            ("S - Move down", text_color),
            ("PLAYER 2", heading_color),
            ("UP ARROW - Move up", text_color),
            ("DOWN ARROW - Move down", text_color),
            ("First to 5 points wins!", WIN_INFO_COLOR),
        ]

        start_y = 155
        line_spacing = 90

        for i, (label, color) in enumerate(lines):
            text = self.text_font.render(label, True, color)
            screen.blit(
                text, text.get_rect(center=(WIDTH // 2, start_y + i * line_spacing))
            )

        # Botón para regresar
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.back_btn.collidepoint(mouse_pos)

        fill_color = FILL_COLOR_HOVERED if hovered else FILL_COLOR
        border_color = BORDER_COLOR_HOVERED if hovered else BORDER_COLOR
        text_color = TEXT_COLOR_HOVERED if hovered else TEXT_COLOR

        # Sombra
        shadow = self.back_btn.move(0, 5)
        pygame.draw.rect(screen, (5, 7, 16), shadow)

        # Botón y borde
        pygame.draw.rect(screen, border_color, self.back_btn)
        inner_rect = self.back_btn.inflate(-6, -6)
        pygame.draw.rect(screen, fill_color, inner_rect)

        # Texto centrado
        text = self.text_font.render("BACK", True, text_color)
        screen.blit(text, text.get_rect(center=self.back_btn.center))

    def handle_event(self, event):
        # Detectar colisiones con los botones (Rectangulos)
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.back_btn.collidepoint(event.pos)
        ):
            return "back"

        return None
