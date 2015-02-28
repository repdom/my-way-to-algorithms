import heapq
import sys

filename = "Median.txt"
lst = [int(l) for l in open(filename)]
H_low = []
H_high = []

sum = 0
for num in lst:
  if len(H_low) > 0:
	if num > -H_low[0]:
	  heapq.heappush(H_high, num)
	else:
	  heapq.heappush(H_low, -num)
  else:
	heapq.heappush(H_low, -num)

  if len(H_low) > len(H_high) + 1:
	heapq.heappush(H_high, -(heapq.heappop(H_low)))
  elif len(H_high) > len(H_low):
	heapq.heappush(H_low, -(heapq.heappop(H_high)))

  sum += -H_low[0]

print sum % 10000