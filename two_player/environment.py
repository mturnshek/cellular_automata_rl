import numpy as np

from two_player.game import Game


class Environment:
    def __init__(self):
        self.game = Game()
        self.rows = self.game.life.rows
        self.cols = self.game.life.cols

    def state(self):
        return self.game.encoded() # board state, move tile counter

    def is_done(self):
        return self.game.is_done()

    def reward(self, player):
        if self.game.winner() == player:
            return 1
        else:
            return 0

    def legal_move_mask(self):
        legal_move_mask = np.zeros((self.rows, self.cols), dtype='bool')
        for i in range(self.rows):
            for j in range(self.cols):
                legal_move_mask[i][j] = self.game.is_legal_move((i, j), self.game.turn)
        return np.ravel(legal_move_mask)

    def step(self, cell):
        return self.game.accept_move(cell)

    def reset(self):
        self.game.reset()
