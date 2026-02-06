class GameStats:
    def __init__(self, settings):
        self.money = settings.starting_money
        self.lives = settings.lives
        self.wave = 1
        self.score = 0
        self.game_over = False

