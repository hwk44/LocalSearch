import numpy as np


def step_gd(current_b, current_m, points, lr):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):  # 임의로 값을 넣으면 확률적 경사하강법
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((current_m * x) + current_b))
        m_gradient += -(2 / N) * x * (y - ((current_m * x) + current_b))
    new_b = current_b - (lr * b_gradient)
    new_m = current_m - (lr * m_gradient)
    return [new_b, new_m]


# Layer 로 b, m
def gd(points, st_b, st_m, lr, iter):  # rate , iterator 하이퍼 파라미터
    b = st_b
    m = st_m
    for i in range(iter):
        b, m = step_gd(b, m, np.array(points), lr)
    return [b, m]


if __name__ == "__main__":
    # 넘파이로 텍스트 읽기
    points = np.genfromtxt("../data/data.csv", delimiter=",")

    # 하강법에 필요한 값 3개
    learning_rate = 0.001
    init_b = 0.5  # 절편
    init_m = 0  # 기울기

    # 반복 횟수?
    num_iter = 1000
    [b, m] = gd(points, init_b, init_m, learning_rate, num_iter)
    print(b)
    print(m)

    # 알고리즘을 만듦
    # 시각화
    #

    # print(points)
