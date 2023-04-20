# import random
#
# import numeric
# import tsp
# LIMITS = 100
# def first_choice(p):
#     current = numeric.random_init(p)
#     value_distance = numeric.evaluate(current, p)  # 최적의 값이라고 가정하고
#
#     i = 0
#     while i < LIMITS:
#
#         pass
#     return current, value_distance
#
# def random_mutant(current, p):
#     DELTA = 0.01
#     # DELTA값 구간 안에 값만 가져옴
#     delta = [-DELTA , DELTA]
#     d = random.choice(delta)
#     pass
#
# def inversion(current, i, j):
#     pass
#
# if __name__ == "__main__":  # __ => entry point 진입 지점
#     p = tsp.create_problem("./data/tsp30.txt")
#     solution, minimum = first_choice(p)
#     print(solution)
#     print(minimum)

#=====================================================================================

from numeric import *

LIMITS = 100


def first_choice(p):
    current = random_init(p)
    values = evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        value_eval = evaluate(successor, p)
        if value_eval < values:
            current = successor
            values = value_eval
            i = 0
        else:
            i += 1
    return current, values


def random_mutant(current, p):
    i = random.randint(0, len(current) - 1)
    delta = [DELTA, -DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)


def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


if __name__ == "__main__":
    p = create_problem("../data/Convex.txt")
    solution, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(solution, minimum)

