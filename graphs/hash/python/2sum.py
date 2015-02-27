import sys
import threading

def main():
    lines = open('algo1-programming_prob-2sum.txt').read().splitlines()
    data = map(lambda x: int(x), lines)

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target