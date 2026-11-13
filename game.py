import pygame
from settings import *
from core.scene_manager import SceneManager
from core.assets_manager import AssetsManager
from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene
from scenes.game_over_scene import GameOverScene
from scenes.help_scene import HelpScene
from scenes.pause_scene import PauseScene

"""
"""


class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.assets_manager = AssetsManager()
        self.scene_manager = None
        self.saved_game = None
        self.winner = None

    def run(self):
        pygame.init()

        pygame.display.set_caption(TITLE)

        # Dibujar el menu inicialmente
        self.scene_manager = SceneManager(MenuScene(self.assets_manager))
        self.scene_manager.scene.draw(self.screen)
        self.assets_manager.intro_sound.play()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            if (
                hasattr(self.scene_manager.scene, "scored")
                and self.scene_manager.scene.scored
            ):
                self.scene_manager.scene.scored = False
                pygame.time.delay(1000)

            action = self.scene_manager.scene.handle_event(event)

            if action == "play":
                self.assets_manager.background_music.play()
                self.scene_manager.change_scene(GameScene(self.assets_manager))
            elif action == "help":
                self.scene_manager.change_scene(HelpScene(self.assets_manager))
            elif action == "leave":
                self.running = False
                break
            elif action == "restart":
                self.assets_manager.background_music.play()
                self.scene_manager.change_scene(GameScene(self.assets_manager))
            elif action == "back":
                self.scene_manager.change_scene(MenuScene(self.assets_manager))
            elif action == "pause":
                self.saved_game = self.scene_manager.scene
                self.scene_manager.change_scene(PauseScene(self.assets_manager))
                pygame.time.delay(250)
            elif action == "resume":
                self.scene_manager.change_scene(self.saved_game)
                self.saved_game = None
                pygame.time.delay(250)

            self.winner = self.scene_manager.scene.update()
            if self.winner is not None:
                game_scene = self.scene_manager.scene
                self.scene_manager.change_scene(
                    GameOverScene(
                        self.winner,
                        game_scene.player1_score,
                        game_scene.player2_score,
                        self.assets_manager,
                    )
                )
                self.assets_manager.game_over_sound.play()

            self.scene_manager.scene.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
