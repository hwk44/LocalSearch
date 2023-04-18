import random
## 본인이 작성 가능해야함
## 읽기 좋게 짜기

'''
간단한 언덕 등반 알고리즘
Convex.txt 를 사용해서 계산
1. 파일을 읽어옴
2. 파일로 초기값을 생성함
3. Convex.txt 파일의 수식과 값을 이용해서 계산
'''


# "./data/Convex.txt"
# def create_problem(filename):
#     # 1-1 파일을 읽자
#     ini_file = open(filename, 'r', encoding='UTF8')
#     expression = ini_file.readline().strip()
#     # 리스트
#     var_names = []
#     lows = []
#     up = []
#     for line in ini_file.readlines():
#         _temp = line.split(",")
#         var_names.append(_temp[0])
#         lows.append(float(_temp[1]))
#         up.append(_temp[2])
#
#     ini_file.close()
#     domain = [var_names, lows, up]
#     return (expression, domain)
#
# def random_init(p):
#     expression, domain = p
#     init = []
#     for i in range(0, len(domain[0])):
#         # 랜덤 선택
#         init.append(random.uniform(domain[1][i], domain[2][i])) # lows ~ up 사이 랜덤 정수
#     return init
#
#
# def evaluate(state, p):
#     num_eval = 0
#     expression = p[0] # 튜플이라고 가정하고
#     var_name = p[1][0]
#
#     for i in range(len(var_name)):
#         assignment = var_name[i] + '=' + str(state[i])
#         exec(assignment) # exec 문자열을 코드로 실행
#
#     return eval(expression)
#
# print(create_problem("./data/Convex.txt"))
# print(random)
#
#
#
# if __name__ == "__main__":
#     p = create_problem("./data/Convex.txt")
#     pass
#     print(create_problem("./data/Convex.txt"))
#     print(1)


import random


def create_problem(filename):
    f = open(filename, "r")
    expression = f.readline()

    var_names = []
    low = []
    up = []

    for line in f.readlines():
        _temp = line.split(",")
        var_names.append(_temp[0])
        low.append(float(_temp[1]))
        up.append(float(_temp[2]))
    domain = [var_names, low, up]
    return (expression, domain)


def random_init(p):
    domain = p[1]
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init


def evaluate(current, p):
    expr = p[0]
    var_names = p[1][0]
    for i in range(len(var_names)):
        assignment = var_names[i] + "=" + str(current[i])
        exec(assignment)
    return eval(expr)


def describe_problem(p):
    print()
    print("Objective function:")
    print(p[0])
    print("Search space:")
    var_names = p[1][0]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(f" {var_names[i]} : {low[i], up[i]}")


# def display_result(solution, minimum):
#     print()
#     print("Solution found:")
#     print(coordinate(solution))  # Convert list to tuple
#     print("Minimum value: {0:,.3f}".format(minimum))
#     print()
#     print("Total number of evaluations: {0:,}".format(NumEval))


def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)


if __name__ == "__main__": #  __ => entry point 진입 지점
    # 식과 인자를 분리
    p = create_problem("./data/Convex.txt")
    # 식과 인자를 출력
    describe_problem(p)
    # 초기값 결정
    solution = random_init(p)
    # 초기값과 식과 인자를 이용해서 계산
    minimum = evaluate(solution, p)
    # 가장 작은 값을 반환
    print(f"{minimum}")

