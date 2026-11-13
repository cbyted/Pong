class SceneManager:
    def __init__(self, game_scene):
        self.scene = game_scene

    def change_scene(self, new_scene):
        self.scene = new_scene

    def handle_event(self, event):
        return self.scene.handle_event(event)

    def update(self, screen):
        return self.scene.update()

    def draw(self, screen):
        return self.scene.draw(screen)
