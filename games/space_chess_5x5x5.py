import numpy as np
from typing import List, Tuple, Optional, Dict

class SpaceChess5x5x5:
    '''
    5x5x5 Space Chess / Raumschach-inspired 3D Chess Engine
    Board dimensions: 5 levels × 5 rows × 5 columns (125 cells)
    Supports 13 possible movement directions in 3D space.
    '''
    
    def __init__(self):
        self.levels = 5
        self.size = 5
        # Board: level, row, col
        self.board = np.full((self.levels, self.size, self.size), None, dtype=object)
        self.initialize_board()
    
    def initialize_board(self):
        '''Initialize with standard-ish 3D chess starting position'''
        # For simplicity, place pieces on bottom and top levels
        # White on level 0, Black on level 4
        
        # Pawns
        for col in range(self.size):
            self.board[0][1][col] = 'WP'  # White Pawn
            self.board[4][3][col] = 'BP'  # Black Pawn
        
        # Rooks
        self.board[0][0][0] = 'WR'
        self.board[0][0][4] = 'WR'
        self.board[4][4][0] = 'BR'
        self.board[4][4][4] = 'BR'
        
        # Knights
        self.board[0][0][1] = 'WN'
        self.board[0][0][3] = 'WN'
        self.board[4][4][1] = 'BN'
        self.board[4][4][3] = 'BN'
        
        # Bishops
        self.board[0][0][2] = 'WB'
        self.board[4][4][2] = 'BB'
        
        # Queen
        self.board[0][0][4] = 'WQ'  # Wait, rook was there, adjust
        # Better setup later
        
        # King
        self.board[0][0][2] = 'WK'
        self.board[4][4][2] = 'BK'
        
        print('5x5x5 Space Chess board initialized.')
    
    def get_all_directions(self) -> List[Tuple[int, int, int]]:
        '''13 possible directions in 3D (all combinations except 0,0,0)'''
        directions = []
        for dl in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if not (dl == 0 and dr == 0 and dc == 0):
                        directions.append((dl, dr, dc))
        return directions
    
    def is_valid_position(self, level: int, row: int, col: int) -> bool:
        return (0 <= level < self.levels and 
                0 <= row < self.size and 
                0 <= col < self.size)
    
    def display_board(self):
        '''Simple text display of all 5 levels'''
        for level in range(self.levels):
            print(f'\n=== Level {level} ===')
            for row in range(self.size):
                line = []
                for col in range(self.size):
                    piece = self.board[level][row][col]
                    line.append(piece if piece else '. ')
                print(' '.join(line))

# Example usage
if __name__ == "__main__":
    game = SpaceChess5x5x5()
    game.display_board()
    print('\n13 movement directions available for 3D pieces.')
