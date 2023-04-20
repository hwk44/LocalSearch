import itertools
from util import *

class BruteForceSolver:
    def __init__(self, cities):   #
        self.cities = cities
        self.total = len(cities)
        self.best_order = []
        self.best_distance = float('inf') # 길이가 무한대

    def find(self):
        start = [i for i in range(self.total)]
        for order in itertools.permutations(start):
            d = calc_path_distance(self.cities, order) # 거리
            if d < self.best_distance:
                self.best_distance = d
                self.best_order = list(order)

    pass

