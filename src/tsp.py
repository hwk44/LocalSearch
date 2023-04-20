a = []
## tsp30 파일 수식이 없음
'''
 그래프 => TSP 
 TSP => 간선의 합이 최소임을 원함
 
 간선과 정점으로 구성된 자료구조
 여기서는 간선 중심으로 보자
 - 방향성이 있는 것 => 네트워크
 - 방향성이 없는 것 => 순수 그래프(조합 그래프)
 정점
 간선
 
 
'''


def create_problem(filename):
    f = open(filename, "r")
    num_cities = int(f.readline())

    locations = []
    for line in f.readlines():
        # 좌표(x,y)는 튜플로 만든다.
        locations.append(eval(line))

    f.close()
    table = create_distance_table(num_cities, locations)
    return num_cities, locations, table



import random
import math

def create_distance_table(num_cities, locations):
    # TODO :
    # 그래프는 어떻게 표현하나요?
    # 그래프 인접행렬로 만듦
    # 관례에 따라 간선의 길이는 1로 한다.
    # 맨해튼 거리 격자(grid world) 로 바꿔야한다.
    # 여기서는 유클리드 거리.


    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            distance = math.sqrt(
                ((locations[i][0] - locations[k][0])**2 +
                (locations[i][1] - locations[k][1])**2)
            )
            line.append(distance)
        table.append(line)
    return table

def random_init(p): # 좌표를 랜덤으로 가져와야함
    # 결과 : shuffle 해서 나온 것
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init # == > current location 배열


def evaluate(current, p):
    cost =0
    num_cities, locations, table = p
    for i in range(num_cities):
        cost += table[current[i]][current[i-1]]
    return cost
    # cost 출력

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of cities : {n}")
    locations = p[1]
    table = p[2]
    for i in range(n):
        print(f'{locations[i]}')
        if i % 5 == 4:
            print()
    print(table)


def coordinate(solution):
    pass


if __name__ == "__main__":  # __ => entry point 진입 지점
    p = create_problem("../data/tsp30.txt")
    # print(p[0])
    # print(p[1])
    # print(p[2])

    # print(describe_problem(p))
    init = random_init(p)
    print(evaluate(init, p))