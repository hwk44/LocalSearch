from util import *
from algo import BruteForce

ALGO_INFO = [
    {
        "name" : "Brute Algo",
        "displacement" : (0, FONT_HEIGHT),
        "name_coords" : (0,0),
        "lenth_coords" : (0,HEIGHT + FONT_HEIGHT),
        "depends" : -1,# 의존성 존재하지 않음 단독 코어로 돌림
        "sim" : BruteForce.BruteForceSolver
    },
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT),
    (WIDTH, 0 , WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0 , WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0 , WIDTH, WINDOW_HEIGHT),
]

