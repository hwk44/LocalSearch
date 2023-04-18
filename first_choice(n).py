import random

import numeric
import tsp
LIMITS = 100
def first_choice(p):
    current = numeric.random_init(p)
    value_distance = numeric.evaluate(current, p)  # 최적의 값이라고 가정하고

    i = 0
    while i < LIMITS:

        pass
    return current, value_distance

def random_mutant(current, p):
    DELTA = 0.01
    # DELTA값 구간 안에 값만 가져옴
    delta = [-DELTA , DELTA]
    d = random.choice(delta)
    pass

def inversion(current, i, j):
    pass

if __name__ == "__main__":  # __ => entry point 진입 지점
    p = tsp.create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)