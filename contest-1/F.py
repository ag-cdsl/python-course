"""
Silent Classroom
https://codeforces.com/contest/1166/problem/A
"""


from collections import Counter


n = int(input())
names = [input() for _ in range(n)]

letters = [name[0] for name in names]
counter = Counter(letters)


def n_pairs(x):
    return x * (x - 1) // 2


n_cursed_pairs = 0
for v in counter.values():
    q, r = divmod(v, 2)
    n_cursed_pairs += n_pairs(q) + n_pairs(q + r)

print(n_cursed_pairs)
