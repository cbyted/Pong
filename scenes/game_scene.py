import pygame
from entities.ball import ball
from entities.paddle import Paddle
from settings import (
    WIDTH,
    HEIGHT,
    PLAYER1_COORD_X,
    PLAYER1_COORD_Y,
    PLAYER2_COORD_X,
    PLAYER2_COORD_Y,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_SPEED,
    BALL_SIZE,
    BALL_SPEED,
    BALL_COORD_X,
    BALL_COORD_Y,
    WHITE,
    GREEN,
    WINNING_SCORE,
)


class GameScene:
    def __init__(self, assets):
        self.assets = assets
        self.background = self.assets.get_bg_img()
        self.score_font = self.assets.get_font(60)

        self.player_bounds = [0, HEIGHT - PADDLE_HEIGHT]
        self.ball_bounds = [BALL_SIZE, HEIGHT - BALL_SIZE]

        # Definir objetos para los jugadores y la pelota
        self.player1 = Paddle(
            PLAYER1_COORD_X,
            PLAYER1_COORD_Y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            PADDLE_SPEED,
            self.player_bounds,
        )
        self.player2 = Paddle(
            PLAYER2_COORD_X,
            PLAYER2_COORD_Y,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
            PADDLE_SPEED,
            self.player_bounds,
        )
        self.ball = ball(
            BALL_COORD_X,
            BALL_COORD_Y,
            BALL_SIZE,
            BALL_SPEED,
            self.ball_bounds,
        )

        self.scored = False
        self.player1_score = 0
        self.player2_score = 0

    def restore_players_pos(self):
        self.player1.start_pos(PLAYER1_COORD_Y)
        self.player2.start_pos(PLAYER2_COORD_Y)

    def handle_event(self, event):
        # Tecla escape para pausar el juego
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "pause"
        return None

    def update(self):
        keys = pygame.key.get_pressed()

        # Jugador 1: w-s
        if keys[pygame.K_w]:
            self.player1.move("UP")
        if keys[pygame.K_s]:
            self.player1.move("DOWN")

        # Jugador 2: Arrow up - Arrow down
        if keys[pygame.K_UP]:
            self.player2.move("UP")
        if keys[pygame.K_DOWN]:
            self.player2.move("DOWN")

        # Movimiento de la bola
        self.ball.move()

        # Punto para el jugador 1
        if self.ball.pos[0] < BALL_SIZE:
            self.ball.pos = [BALL_COORD_X, BALL_COORD_Y]
            self.ball.speed_x *= -1
            self.player1_score += 1
            self.scored = True
            self.restore_players_pos()
            self.assets.score_sound.play()

        # Punto para el jugador 2
        if self.ball.pos[0] > WIDTH:
            self.ball.pos = [BALL_COORD_X, BALL_COORD_Y]
            self.ball.speed_x *= -1
            self.player2_score += 1
            self.scored = True
            self.restore_players_pos()
            self.assets.score_sound.play()

        if self.player1_score >= WINNING_SCORE:
            return "Player 1"
        if self.player2_score >= WINNING_SCORE:
            return "Player 2"

        if self.player1.get_rect().colliderect(self.ball.get_rect()):
            self.ball.bounce(self.assets.bounce_sound)

        if self.player2.get_rect().colliderect(self.ball.get_rect()):
            self.ball.bounce(self.assets.bounce_sound)

        return None

    def draw_score(self, screen):
        player1_score_text = self.score_font.render(
            str(self.player1_score), True, WHITE
        )
        player2_score_text = self.score_font.render(
            str(self.player2_score), True, WHITE
        )

        screen.blit(
            player1_score_text,
            player1_score_text.get_rect(center=(WIDTH // 2 + 100, 50)),
        )
        screen.blit(
            player2_score_text,
            player2_score_text.get_rect(center=(WIDTH // 2 - 100, 50)),
        )

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.player1.draw(screen, WHITE)
        self.player2.draw(screen, WHITE)
        self.ball.draw(screen, GREEN)
        self.draw_score(screen)
