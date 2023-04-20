import threading

import pygame
from algo_info import ALGO_INFO, DIVIDERS
import gfx
from util import *

# 0. 알고리즘을 어떻게 되었든 먼저 만들어야 하는거 아닌가
# 1. 좌표를 찍자
# 2. loop를 만들어야 한다.
#
#
def loop():
    for i in range(len(ALGO_INFO)):
        print(ALGO_INFO[i])
    while True:
        gfx.check_events()
        # gfx.draw_text_center(surface, "Hello", font, 50, 50)
        gfx.draw_dividers(surface, DIVIDERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                gfx.draw_text_top_left(surface,
                                       ALGO_INFO[i]["name"],
                                       GREEN,
                                       font,
                                       *ALGO_INFO[i]["name_coords"])
                gfx.draw_path(surface, list_of_cities_list[i], sim[i].best_order)
            elif len(sim[ALGO_INFO[i]["depends"].best_order != 0]):
                
                pass
        pygame.display.update()
        surface.fill(BLACK)

    # 1. 애니메이션 나오게 하고 싶어요. 집에 가기 전까지
    # 1. p를 내가 만들어야 함 (랜덤으로 만듦) => 답이 있는 램덤으로 만듬
    # 모든 도시들이 순회 가능하도록
    # 1.2 포팅
    #
    #
    #

    # 1. 알고리즘 정보 가져온다.
    # 2. 무한반복
    # 2-1. 알고리즘을 배치한다.
    # 2-2. 그리면 된다. ==> 뭐라고?
    # 점, 선, 텍스트
    # draw_point(x,y) => 값 반환하지 않음
    # draw_line(x,y) => 값 반환하지 않음
    # draw_text(x,y) => 값 반환하지 않음
pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)
cities = make_cities(20)
# graph = make_graph_from_city_list(cities)
list_of_cities_list = []
sim = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sim[i].find))
        threads[i].daemon = True

if __name__ == "__main__":
    pygame.display.set_caption("TSP - Visualizer")

    # print(ALGO_INFO)
    # print(ALGO_INFO[i]["displacement"])
    # loop()
    # print(cities)
    # print(graph)
    # 첫번째 시작 위치
    # 두번째 시작 위치
