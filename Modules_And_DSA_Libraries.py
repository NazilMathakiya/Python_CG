# import
import math

print(math.sqrt(25))  #5.0
print(math.factorial(5))  #120


# Import specific functions
from math import sqrt
print(sqrt(25))


# as
import math as m
print(m.sqrt(25))


# Counter
from collections import Counter

arr = [1, 2, 2, 3, 3, 3]
freq = Counter(arr)
print(freq)
print(freq[3])


# defaultdict
from collections import defaultdict

freq = defaultdict(int)
for x in [1, 2, 2, 3]:
    freq[x] += 1
print(freq)


# deque
from collections import deque

q = deque()

q.append(10)
q.append(20)

print(q.popleft())


# heapq
import heapq

heap = [5, 2, 8, 1]

heapq.heapify(heap)

print(heapq.heappop(heap))



# bisect
import bisect

arr = [1, 3, 5, 7]

index = bisect.bisect_left(arr, 5)

print(index)



# itertools
from itertools import permutations

arr = [1, 2, 3]

print(list(permutations(arr)))



