import pygame
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
    GAME_OVER_COLOR,
    WINNER_COLOR,
    SCORE_TEXT_COLOR,
)


class GameOverScene:
    def __init__(self, winner, player1_score, player2_score, assets):
        self.assets = assets

        self.title_font = self.assets.get_font(64)
        self.text_font = self.assets.get_font(28)

        self.winner = winner
        self.player1_score = player1_score
        self.player2_score = player2_score

        self.restart_btn = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.back_btn = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.buttons = [
            (self.back_btn, "BACK", "back"),
            (self.restart_btn, "RESTART", "restart"),
        ]

        self.restart_btn.center = (WIDTH // 2, HEIGHT // 2 + 100)
        self.back_btn.center = (WIDTH // 2, HEIGHT // 2 + 200)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render("GAME OVER", True, GAME_OVER_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 4)))

        winner_text = self.text_font.render(f"{self.winner} WINS!", True, WINNER_COLOR)
        screen.blit(
            winner_text,
            winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 35)),
        )

        score_text = self.text_font.render(
            f"{self.player1_score}  -  {self.player2_score}",
            True,
            SCORE_TEXT_COLOR,
        )

        screen.blit(
            score_text,
            score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 15)),
        )

        mouse_pos = pygame.mouse.get_pos()

        for button, label, _ in self.buttons:
            hovered = button.collidepoint(mouse_pos)

            # Colores según si el cursor está encima
            fill_color = FILL_COLOR_HOVERED if hovered else FILL_COLOR
            border_color = BORDER_COLOR_HOVERED if hovered else BORDER_COLOR
            text_color = TEXT_COLOR_HOVERED if hovered else TEXT_COLOR

            # Sombra desplazada
            shadow = button.move(0, 5)
            pygame.draw.rect(screen, (5, 7, 16), shadow)

            # Botón y borde
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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "restart"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "back"

        return None
