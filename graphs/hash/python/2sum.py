import sys
import threading

def TwoSum(hashtable, target):

    for x in hashtable:
        y =  target - x
        if y in  hashtable and x != y:
            return (x, y)
    return None


def main():
    lines = open('algo1-programming_prob-2sum.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    hashtable = dict()
    for num in data:
        hashtable[num] = True

    count = 0
    for target in range(-10000,10000+1):
        if TwoSum(hashtable, target):
            count += 1
    print count

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target