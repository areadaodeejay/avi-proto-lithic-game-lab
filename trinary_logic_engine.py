import itertools

class TrinaryLogic:
    """Standard Trinary Logic Engine using 0=False, 1=Unknown, 2=True"""
    
    FALSE = 0
    UNKNOWN = 1
    TRUE = 2
    
    @staticmethod
    def NOT(a):
        if a == 0: return 2
        if a == 2: return 0
        return 1  # Unknown remains unknown
    
    @staticmethod
    def AND(a, b):
        return min(a, b)
    
    @staticmethod
    def OR(a, b):
        return max(a, b)
    
    @staticmethod
    def XOR(a, b):
        if a == b: return 0
        if 1 in (a, b): return 1
        return 2 if (a == 0 and b == 2) or (a == 2 and b == 0) else 1
    
    @staticmethod
    def IMPLIES(a, b):
        # a → b
        return TrinaryLogic.OR(TrinaryLogic.NOT(a), b)
    
    @staticmethod
    def generate_truth_table(operator, num_inputs=2):
        values = [0, 1, 2]
        inputs = list(itertools.product(values, repeat=num_inputs))
        print(f"\nTruth Table for {operator.__name__}:")
        print(" | ".join([f"x{i}" for i in range(1, num_inputs+1)] + ["Output"]))
        print("-" * 40)
        for inp in inputs:
            if num_inputs == 1:
                result = operator(inp[0])
            else:
                result = operator(*inp)
            print(" | ".join([str(x) for x in inp] + [str(result)]))

# Example usage
if __name__ == "__main__":
    print("=== Trinary Logic Engine (0=False, 1=Unknown, 2=True) ===")
    TrinaryLogic.generate_truth_table(TrinaryLogic.AND)
    TrinaryLogic.generate_truth_table(TrinaryLogic.OR)
    TrinaryLogic.generate_truth_table(TrinaryLogic.NOT, 1)
    
    # Game example
    player_health = TrinaryLogic.TRUE
    enemy_near = TrinaryLogic.UNKNOWN
    should_attack = TrinaryLogic.AND(player_health, TrinaryLogic.NOT(enemy_near))
    print(f"\nGame Decision - Should Attack: {should_attack}")