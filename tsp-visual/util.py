import pygame.math
import random

WIDTH = 300
HEIGHT = 300
FONT_HEIGHT = 20
WINDOW_HEIGHT = 800

WINDOW_WIDTH = WIDTH * 4
WIDTH_HEIGHT = (HEIGHT + FONT_HEIGHT + FONT_HEIGHT) * 2
WINDOW_X = 10
WINDOW_Y = 10

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CITY_SIZE = 300
MIN_CITY_SIZE = 7.5
MAX_CITY_SIZE = 10
def make_cities(total_cities):
    cities = [] # 도시 좌표가 필요함
    r = CITY_SIZE // total_cities # 간격 유지
    for i in range(total_cities):
        cities.append(
            pygame.math.Vector2(random.randrange(r, WIDTH -r),
                                          random.randrange(r, HEIGHT - r))
        )

    # 겹치지 않으면서 문제를 풀고싶음
    return cities

def make_graph_from_city_list(cities):
    n = len(cities)
    graph = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        # 간선 연결
        city_a = cities[i]
        for j in range(i, n):
            if i == j:
                graph[i][j] = 0
            else:
                city_b = cities[j]

                d = (city_a - city_b).length()
                graph[i][j] = graph[i][j] = d
    return graph

def calc_path_distance(points, order):
    dist =0
    for i in range(len(order)):
        city_a = points[order[i% len(order)]]
        city_b = points[order[(i+1)% len(order)]]
        d = (city_a - city_b).length()
        dist += d
    return dist

def displace(cities, x, y):
    new = []
    displaceVector = pygame.math.Vector2(x,y)
    for c in displaceVector:
        new.append(c + displaceVector)
    return new