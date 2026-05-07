# Ternary Logic Engine for Game Development
# Created with Grok for avi-proto-lithic-game-lab
# Supports both standard ternary (0,1,2) and balanced ternary (-1,0,1)

class Ternary:
    def __init__(self, value):
        if value not in [-1, 0, 1, 2]:
            raise ValueError("Ternary value must be -1, 0, 1, or 2")
        self.value = value
    
    def __repr__(self):
        return f"T({self.value})"

# Basic Ternary Logic Gates (using Kleene's strong logic for 3-valued logic)
def tern_not(a):
    if a == 0: return 2
    if a == 2: return 0
    return 1  # Unknown stays unknown

def tern_and(a, b):
    return min(a, b) if isinstance(a, int) and isinstance(b, int) else 0

def tern_or(a, b):
    return max(a, b)

# Balanced Ternary operations (more useful for arithmetic)
class BalancedTernary:
    def __init__(self, value=0):
        self.value = max(min(int(value), 1), -1)
    
    def __add__(self, other):
        # Simple implementation - can be expanded
        return BalancedTernary(self.value + other.value)
    
    def __mul__(self, other):
        return BalancedTernary(self.value * other.value)

# Example usage for games (e.g. Frequency Warriors chess logic)
def simulate_ternary_chess_outcome(player_strength, opponent_strength):
    '''Returns 2 = strong win, 1 = uncertain, 0 = loss'''
    if player_strength > opponent_strength:
        return 2
    elif player_strength < opponent_strength:
        return 0
    else:
        return 1

print("Ternary Logic Engine Loaded")
print("Example: NOT(2) =", tern_not(2))
print("AND(2,1) =", tern_and(2,1))

# Test
a = Ternary(2)
print(a)