from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_first_statement = And(AKnight, AKnave)

knowledge0 = And(
    # A, B, and C can only be a knight or a knave, not both.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Two-way implications.
    Biconditional(AKnight, A_first_statement)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_second_statement = And(AKnave, BKnave)

knowledge1 = And(
    # A, B, and C can only be a knight or a knave, not both.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Two-way implications.
    Biconditional(AKnight, A_second_statement)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_third_statement = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_first_statement = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # A, B, and C can only be a knight or a knave, not both.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Two-way implications.
    Biconditional(AKnight, A_third_statement),
    Biconditional(BKnight, B_first_statement)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_fourth_statement = Biconditional(AKnight, Not(AKnave))
B_SecondAndThird_statement = And(Biconditional(AKnave, BKnight), CKnave)
C_first_statement = AKnight

knowledge3 = And(
    # A, B, and C can only be a knight or a knave, not both.
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Two-way implications.
    Biconditional(AKnight, A_fourth_statement),
    Biconditional(BKnight, B_SecondAndThird_statement),
    Biconditional(CKnight, C_first_statement)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
