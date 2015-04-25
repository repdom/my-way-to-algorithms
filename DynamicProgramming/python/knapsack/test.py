import collections
import itertools
import sys
import threading

Item = collections.namedtuple('Item', ['value', 'weight'])

def read_data(filename):
    items = []
    capacity, item_cnt = 0, 0
    with open(filename) as f:
        first_line = f.readline().strip().split(' ')
        capacity, item_cnt = int(first_line[0]), int(first_line[1])
        for line in f:
            value, weight = line.strip().split(' ')
            items.append(Item(int(value), int(weight)))
    return capacity, items

class Memorize(object):
    def __init__(self):
        self.hits = 0
        self.miss = 0
        self.cache = {}

    def __call__(self, func):

        def wrapper(*args):
            if args in self.cache:
                self.hits += 1
            else:
                self.miss += 1
                self.cache[args] = func(*args)
            return self.cache[args]
        return wrapper

mm = Memorize()

def knapsack(capacity, items):

    def inner(capa, j):
        #print capa, j
        if (capa, j) in mm.cache:
            mm.hits += 1
            return mm.cache[(capa, j)]

        result = 0
        if capa < 0:
            result = 0
        elif j == 0:
            if capa >= items[0].weight:
                result = items[0].value
            else:
                result = 0
        else:
            w1 = inner(capa, j - 1)
            if capa >= items[j].weight:
                w2 = inner(capa - items[j].weight, j - 1) + items[j].value
            else:
                w2 = 0
            result =  max(w1, w2)
        mm.cache[(capa, j)] = result
        mm.miss += 1
        return result
    return inner(capacity, len(items) -1)

def main():
    capacity, items = read_data('knapsack_big.txt')
    print knapsack(capacity, items)
    print 'hits: %s, miss: %s' % (mm.hits, mm.miss)

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target