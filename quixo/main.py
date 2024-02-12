import random
import pickle
from game import Game, Move, Player, Board


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move


class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.cache = {}
        self.cnt_move = 0

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        board = Board(game.get_board())
        best = float('-inf')
        available_moves = self.get_available_moves(board, 1)
        best_moves = []
        self.cnt_move += 1

        if self.cnt_move > 10:
            depth = 2
        else:
            depth = 1

        for move in available_moves:
            temp_board = Board(board.get_board())
            temp_board.move(move[0], move[1], 1)
            res = self.recursive_minimax(temp_board, 0, depth)

            if res > 0:
                from_pos, slide = move
                return from_pos, slide
            
            elif res > best:
                best = res
                best_moves.clear()
                best_moves.append(move)

            elif res == best:
                best_moves.append(move)

        from_pos, slide = random.choice(tuple(best_moves))

        return from_pos, slide
    
    def get_available_moves(self, board: Board, player_id: int) -> list[tuple[tuple[int, int], Move]]:
        available_moves = []
        
        for i in range(5):
            for move in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                available = board.check_move((i, 0), move, player_id)
                if available:
                    available_moves.append(((0, i), move))

        for i in range(5):
            for move in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                available = board.check_move((i, 4), move, player_id)
                if available:
                    available_moves.append(((4, i), move))

        for i in range(1,4):
            for move in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                available = board.check_move((0, i), move, player_id)
                if available:
                    available_moves.append(((i, 0), move))

        for i in range(1,4):
            for move in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                available = board.check_move((4, i), move, player_id)
                if available:
                    available_moves.append(((i, 4), move))

        return available_moves
    
    def recursive_minimax(self, board: Board, is_maximizing_player: int, deep: int):
        evaluation = self.evaluate(board, deep)
        if evaluation is not None:
            return evaluation

        available_moves = self.get_available_moves(board, is_maximizing_player)

        evaluation_function = max if is_maximizing_player else min
        evaluation = float('-inf') if is_maximizing_player else float('inf')

        for move in available_moves:
            temp_board = Board(board.get_board())
            temp_board.move(move[0], move[1], is_maximizing_player)
            res = self.recursive_minimax(temp_board, 1 - is_maximizing_player, deep - 1)
            evaluation = evaluation_function(evaluation, res)
            if (is_maximizing_player and evaluation > 0) or (not is_maximizing_player and evaluation < 0):
                break

        self.cache[hash(str(board.get_board().tolist()))] = evaluation

        return evaluation
    
    def evaluate(self, board: Board, deep: int):
        winner = board.check_winner() 
        if winner == 0:
            return -1
        
        if winner == 1:
            return 1
        
        if deep == 0:
            return 0
        
        board_hash = hash(str(board.get_board().tolist()))
        if board_hash in self.cache:
            return self.cache[board_hash]
        
        return None
    
    def save_cache(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.cache, file)

    def load_cache(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.cache = pickle.load(file)
        except FileNotFoundError:
                self.cache = {}
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred while loading the cache: {e}")

if __name__ == '__main__':
    wins = [0, 0]

    for i in range(100):
        g = Game()
        player1 = RandomPlayer()
        player2 = MyPlayer()
        player2.load_cache("cache")
        wins[g.play(player1, player2)] += 1
        player2.save_cache("cache")
        print(i)
        
    print(f"My Player won {wins[1]} times")
    print(f"Random Player won {wins[0]} times")
