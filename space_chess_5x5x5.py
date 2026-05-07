import numpy as np
from typing import List, Tuple, Optional, Dict
from enum import Enum

class PieceType(Enum):
    KING = 'K'
    QUEEN = 'Q'
    ROOK = 'R'
    BISHOP = 'B'
    KNIGHT = 'N'
    PAWN = 'P'
    VOID = '·'  # Empty space

class SpaceChess:
    def __init__(self):
        self.board = self._create_empty_board()
        self.current_player = 'white'
        self.move_history = []

    def _create_empty_board(self) -> np.ndarray:
        """Create 5x5x5 board: dimensions [z][y][x]"""
        board = np.full((5, 5, 5), None, dtype=object)
        return board

    def print_board(self):
        """Print the 5x5x5 board layer by layer"""
        print("\n=== 5x5x5 SPACE CHESS ===\n")
        for z in range(5):
            print(f"Layer {z} (Z={z})")
            for y in range(5):
                row = []
                for x in range(5):
                    piece = self.board[z][y][x]
                    if piece is None:
                        row.append('·')
                    else:
                        row.append(piece)
                print(' '.join(row))
            print("-" * 20)

    def is_valid_position(self, z: int, y: int, x: int) -> bool:
        return 0 <= z < 5 and 0 <= y < 5 and 0 <= x < 5

    # 13 possible movement directions in 3D space
    def get_directions(self) -> List[Tuple[int, int, int]]:
        directions = []
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dz == 0 and dy == 0 and dx == 0:
                        continue
                    directions.append((dz, dy, dx))
        return directions  # 26 directions actually, but many games use this

# Example setup function
def setup_demo_board():
    game = SpaceChess()
    # Add some demo pieces
    # White pieces on bottom layers
    game.board[0][4][2] = '♔'  # White King
    game.board[0][4][0] = '♖'  # White Rook
    game.board[1][2][2] = '♕'  # White Queen on higher layer
    # Black pieces
    game.board[4][0][2] = '♚'  # Black King
    return game

if __name__ == "__main__":
    print("5x5x5 Space Chess Engine - Proto-Lithic Edition")
    game = setup_demo_board()
    game.print_board()
    print("\n13+ directional 3D movement system ready for Frequency Warriors integration.")
    print("Ready for full rules, AI, and ternary logic integration.")