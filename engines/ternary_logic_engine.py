import numpy as np
from typing import Literal, Union

TernaryValue = Literal[-1, 0, 1]

class TernaryLogicEngine:
    '''
    Ternary Logic Engine for advanced game AI, decision systems,
    and simulation with uncertainty (e.g. Frequency Warriors).
    Uses balanced ternary: -1 = False/Negative, 0 = Unknown/Maybe, 1 = True/Positive
    '''
    
    @staticmethod
    def NOT(a: TernaryValue) -> TernaryValue:
        '''Ternary NOT'''
        return -a if a != 0 else 0
    
    @staticmethod
    def AND(a: TernaryValue, b: TernaryValue) -> TernaryValue:
        '''Ternary AND (min)'''
        return min(a, b)
    
    @staticmethod
    def OR(a: TernaryValue, b: TernaryValue) -> TernaryValue:
        '''Ternary OR (max)'''
        return max(a, b)
    
    @staticmethod
    def XOR(a: TernaryValue, b: TernaryValue) -> TernaryValue:
        '''Ternary XOR'''
        if a == b:
            return 0
        return a if b == 0 else b if a == 0 else -a if a == -b else 0
    
    @staticmethod
    def implication(a: TernaryValue, b: TernaryValue) -> TernaryValue:
        '''a → b'''
        return TernaryLogicEngine.OR(TernaryLogicEngine.NOT(a), b)
    
    @staticmethod
    def to_binary(t: TernaryValue) -> int:
        '''Convert to crisp binary (for final decisions)'''
        return 1 if t > 0 else 0
    
    @staticmethod
    def from_probability(p: float) -> TernaryValue:
        '''Convert probability to ternary state'''
        if p > 0.7:
            return 1
        elif p < 0.3:
            return -1
        else:
            return 0

# Example usage
if __name__ == "__main__":
    engine = TernaryLogicEngine
    print('Ternary Logic Engine Ready')
    print('NOT(1)  =', engine.NOT(1))
    print('AND(1, -1) =', engine.AND(1, -1))
    print('OR(0, 1)   =', engine.OR(0, 1))