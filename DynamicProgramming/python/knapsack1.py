import collections
import itertools

Item = collections.namedtuple('Item', ['value', 'weight'])

def read_data(filename):
	items = []
	limit, item_cnt = 0, 0
	with open(filename) as f:
		first_line = f.readline().strip().split(' ')
		limit, item_cnt = int(first_line[0]), int(first_line[1])
		for line in f:
			value, weight = line.strip().split(' ')
			items.append(Item(int(value), int(weight)))
	return limit, items

def knapsack(items, limit):
	table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

	for j in xrange(1, len(items) + 1):
		val, wt = items[j-1]
		for w in xrange(1, limit + 1):
			if wt > w:
				table[j][w] = table[j-1][w]
			else:
				table[j][w] = max(table[j-1][w],
								  table[j-1][w-wt] + val)

	result = []
	w = limit
	for j in range(len(items), 0, -1):
		was_added = table[j][w] != table[j-1][w]

		if was_added:
			val, wt = items[j-1]
			result.append(items[j-1])
			w -= wt

	return result

def main():
	capacity, items = read_data('knapsack1.txt')
	print knapsack(items, limt)

if __name__ == '__main__':
	main()
