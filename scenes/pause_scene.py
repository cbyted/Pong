import pygame
from pathlib import Path
from settings import (
    WIDTH,
    HEIGHT,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BACKGROUND_COLOR,
    FILL_COLOR,
    FILL_COLOR_HOVERED,
    BORDER_COLOR,
    BORDER_COLOR_HOVERED,
    TEXT_COLOR,
    TEXT_COLOR_HOVERED,
    TITLE_TEXT_COLOR,
)


class PauseScene:
    def __init__(self, assets):
        self.assets = assets

        self.title_font = self.assets.get_font(80)
        self.text_font = self.assets.get_font(36)

        self.back_btn = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.leave_btn = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.back_btn.center = (WIDTH // 2, HEIGHT // 2 + 200)
        self.leave_btn.center = (WIDTH // 2, HEIGHT // 2 + 280)

        self.buttons = [
            (self.back_btn, "BACK", "back"),
            (self.leave_btn, "LEAVE", "leave"),
        ]

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render("= PAUSED =", True, TITLE_TEXT_COLOR)
        screen.blit(
            title,
            title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)),
        )

        text = self.text_font.render("Press esc to resume game", True, TITLE_TEXT_COLOR)
        screen.blit(
            text,
            text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)),
        )

        # Leave button
        mouse_pos = pygame.mouse.get_pos()

        for button, label, _ in self.buttons:
            hovered = button.collidepoint(mouse_pos)

            fill_color = FILL_COLOR_HOVERED if hovered else FILL_COLOR
            border_color = BORDER_COLOR_HOVERED if hovered else BORDER_COLOR
            text_color = TEXT_COLOR_HOVERED if hovered else TEXT_COLOR

            # Sombra
            shadow = button.move(0, 5)
            pygame.draw.rect(screen, (5, 7, 16), shadow)

            # Boton y borde
            pygame.draw.rect(screen, border_color, button)
            inner_rect = button.inflate(-6, -6)
            pygame.draw.rect(screen, fill_color, inner_rect)

            # Texto centrado
            text = self.text_font.render(label, True, text_color)
            screen.blit(text, text.get_rect(center=button.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button, _, action in self.buttons:
                if button.collidepoint(event.pos):
                    return action

        if event.type == pygame.KEYDOWN and (
            event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN
        ):
            return "resume"

        return None

    def update(self):
        pass
