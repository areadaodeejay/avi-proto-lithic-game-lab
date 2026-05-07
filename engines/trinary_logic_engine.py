# trinary_logic_engine.py
# Standard Trinary (Three-Valued) Logic Engine
# Values: 0 = False, 1 = Unknown/Maybe, 2 = True

class Trinary:
    F = 0  # False
    U = 1  # Unknown / Maybe
    T = 2  # True

    @staticmethod
    def not_(a):
        """Trinary NOT"""
        if a == Trinary.F: return Trinary.T
        if a == Trinary.T: return Trinary.F
        return Trinary.U

    @staticmethod
    def and_(a, b):
        """Trinary AND (Kleene's strong logic)"""
        if a == Trinary.F or b == Trinary.F:
            return Trinary.F
        if a == Trinary.U or b == Trinary.U:
            return Trinary.U
        return Trinary.T

    @staticmethod
    def or_(a, b):
        """Trinary OR"""
        if a == Trinary.T or b == Trinary.T:
            return Trinary.T
        if a == Trinary.U or b == Trinary.U:
            return Trinary.U
        return Trinary.F

    @staticmethod
    def implies(a, b):
        """Trinary implication"""
        return Trinary.or_(Trinary.not_(a), b)

    @staticmethod
    def xor(a, b):
        return Trinary.or_(Trinary.and_(a, Trinary.not_(b)), Trinary.and_(Trinary.not_(a), b))

    @staticmethod
    def to_string(value):
        return ["False", "Unknown", "True"][value]


# Example usage and testing
if __name__ == "__main__":
    print("Trinary Logic Engine")
    print("NOT True  →", Trinary.to_string(Trinary.not_(Trinary.T)))
    print("False AND Unknown →", Trinary.to_string(Trinary.and_(Trinary.F, Trinary.U)))
    print("Unknown OR True →", Trinary.to_string(Trinary.or_(Trinary.U, Trinary.T)))

    # Simple truth table example
    print("\nSample AND truth table:")
    for a in [0,1,2]:
        for b in [0,1,2]:
            result = Trinary.and_(a, b)
            print(f"{Trinary.to_string(a)} AND {Trinary.to_string(b)} = {Trinary.to_string(result)}")
