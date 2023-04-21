from numeric import *

ALPHA = 0.01
EPSILON = 0.0001
def steepest_ascent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, value_best_of) = best_of(neighbors, p)
        if value_best_of >= values:
            break
        else:
            current = successor
            values = value_best_of
    return (current, values)


def mutants(current, p):
    neighbors = []
    for i in range(0, len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors


def best_of(neighbors, p):
    all = []
    for i in range(0, len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(min(all))]
    return (best, best_value)


def display_setting():
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print("Update Rate : ", ALPHA)
    print(f"Calculating Derivatives : {EPSILON}")

def gradient(current, p, EPSILON):
    derivate = []
    domain = p[1] # 하한, 상한이 있어야 함 (지역 검색)
    low = domain[1]
    up = domain[2]
    gradient = []
    for i in range(len(current)):
        value = current[i]
        derivate = current[:i]
        if(low[i] <= value + EPSILON <= up[i]): # 상한 하한 안쪽에 있는지?
            value = value + EPSILON # 있으면 조금 노이즈 끼워서 값 저장
        derivate.append(value) # 어펜드
        derivate.extend(current[i + 1 :]) ## neighbor 붙임 tf.flatten
        gradient.append((evaluate(derivate, p) - value) / EPSILON)
    return  gradient



    # 미분은 내가 어떻게 하나요?
    # - 기울기 라는데
    # - 점과 직선의 방정식
    # 미분을 해서 차이는 어떻게 계산?
    # y = ax + b
    # 미분을 해서 차이는 어떻게 계산?

def gradient_descent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        gradient_lst = gradient(current, p, values, EPSILON)
        next_p = take_step(gradient_lst, current)
        next_n = evaluate(next_p, p)
        if next_n <= values:
            values = next_n
            current = next_p
        else:
            break
    return (current, values)


def take_step(current, gradient):
    suc = []
    for i in range(len(current)):
        suc.append(current[i] - gradient[i])
        pass
    return suc

# def take_step(gradient, current):
#     suc = []
#     for i in range(len(current)):
#         suc.append(current[i] - (ALPHA * gradient[i]))
#     return suc


if __name__ == "__main__":
    p = create_problem("../data/Convex.txt")
    # solution, minimum = steepest_ascent(p)
    current = random_init(p)
    values = evaluate(current, p)
    display_setting()
    display_result(current, values)

    print(current, values)

    # while True:
    #     gradient = gradient(current, p, EPSILON)
    #     next_p = take_step(current, gradient)
    #     next_n = evaluate(next_p, p)
    #     if next_n < value:
    #         current = next_p
    #         value = next_n
    #     else:
    #         break


    # describe_problem(p)
    # display_setting()
    # display_result(solution, minimum)

