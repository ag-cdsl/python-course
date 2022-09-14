"""
Taxi
https://codeforces.com/contest/158/problem/B
"""

from collections import Counter
import math


n = int(input())
s = [int(x) for x in input().split()]
n_groups = Counter(s)


n_cars = 0

n_cars += n_groups[4]

n_22 = n_groups[2] // 2
n_cars += n_22
n_groups[2] -= n_22 * 2

n_13 = min(n_groups[1], n_groups[3])
n_cars += n_13
n_groups[1] -= n_13
n_groups[3] -= n_13
n_cars += n_groups[3]

if n_groups[2]:
    n_cars += 1
    n_groups[1] -= min(n_groups[1], 2)
    
n_cars += math.ceil(n_groups[1] / 4)

print(n_cars)
