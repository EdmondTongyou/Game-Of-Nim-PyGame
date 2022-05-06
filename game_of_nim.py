from games import *
class GameOfNim(Game):
    def __init__(self, board = list()):
        self.board = board
        moves = list()
        for index in range(0, len(board)):
            x = index
            moves += ([((x, y)) for y in range(1, board[index] + 1)])
        self.moves = moves
        self.initial = GameState(to_move = "Max", utility = 0, board = board, moves = moves)


    def result(self, state, move):
        board = state.board.copy()
        moves = state.moves.copy()
        if move not in moves:
            return state
        x = board[move[0]]
        deadStates = 0

        # Sets deadStates based off board position - move made
        # Sets board as board position - move made
        deadStates = move[1]
        board[move[0]] = board[move[0]] - move[1]
    
        # If deadStates is 0 then all moves for board position must be removed so x position gets moved
        # Checks if there is only 1 move and only removes that if that is the case
        if deadStates == 0:
            deadStates = move[1]
            x = (moves.index(move) - (moves.index(move) - deadStates - 2))
        if len(moves) == 1:
            moves.remove(moves[0])
        else:
            for index in range(0, deadStates):
                moves.remove(((move[0]), (x-index)))


        return GameState(to_move=('Min' if state.to_move == 'Max' else 'Max'), utility=self.utility(state, state.to_move), board = board, moves = moves)


    def actions(self, state):
        return state.moves


    def terminal_test(self, state):
        if len(state.moves) == 0:
            return True
        return False


    def utility(self, state, player):
        if self.terminal_test(state):
            if player == "Max":
                return +1
            else:
                return -1
        return 0


    def to_move(self, state):
        return state.to_move


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    #print(nim.initial.board) # must be [0, 5, 3, 1] or [7, 5, 3, 1]
    #print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
                            # or [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    #print(nim.result(nim.initial, (1,2))) # initial goes to [7, 2, 3, 1] if (1,3)
    #print(nim.terminal_test(GameState(to_move = "max", utility = 0, board = [0, 0, 0, 1], moves = list())))
    utility = nim.play_game(alpha_beta_player, alpha_beta_player) # computer moves firstpp
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")