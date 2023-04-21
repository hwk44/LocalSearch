# import random
# import tsp
# LIMITS = 100
# def first_choice(p):
#     current = tsp.random_init(p)
#     value_distance = tsp.evaluate(current,p) # 최적의 값이라고 가정하고
#     # 알고리즘 활용해서 최적값을 변경하는 코드
#     # value_distance 이걸 어떻게 줄이나요?
#
#     i=0
#     while i <LIMITS:
#         successor = random_mutant(current, p)
#         _value_distance = tsp.evaluate(successor,p)
#         if _value_distance < value_distance:
#             current = successor
#             value_distance = _value_distance
#             i = 0
#         else:
#             i += 1
#     return current, value_distance
#
# # 변이를 준다는 것
# # todo
# def random_mutant(current, p):
#     while True:
#         # 좌표는 어떻게 받아옴..
#         i, j = sorted([random.randrange(p[0]) for _ in range(2)])
#         if i < j:
#             cur_copy = inversion(current, i, j)
#             break
#     return cur_copy
#
#
# def inversion(current, i, j):
#     cur_copy = current[:] #
#     while i < j :
#         cur_copy[i] , cur_copy[j] = cur_copy[j], cur_copy[i]
#         i += 1
#         j -= 1
#
#
# if __name__ == "__main__":  # __ => entry point 진입 지점
#     p = tsp.create_problem("./data/tsp30.txt")
#     solution, minimum = first_choice(p)
#     print(solution)
#     print(minimum)
from src.numeric import display_result
# =========================================================================================================

from tsp import *

LIMITS = 100


def first_choice(p):
    current = random_init(p)
    values = evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        values_eval = evaluate(successor, p)
        if values_eval < values:
            current = successor
            values = values_eval
            i = 0
        else:
            i += 1
    return current, values


def random_mutant(current, p):
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            current_copy = inversion(current, i, j)
            break
    return current_copy


def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")


if __name__ == "__main__":
    p = create_problem("../data/tsp30.txt")
    solution, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(solution, minimum)

