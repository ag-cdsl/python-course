"""
Love Triangle
https://codeforces.com/contest/939/problem/A
"""

n = int(input())
f = [int(x) for x in input().split()]


visited = set()
for i in range(n):
    if i in visited:
        continue
    visited.add(i)
    
    cycle = {}
    j = i
    idx = 0
    while j not in cycle:
        cycle[j] = idx
        visited.add(j)
        j = f[j] - 1
        idx += 1
    if idx - cycle[j] == 3:
        print('YES')
        break
else:
    print('NO')
