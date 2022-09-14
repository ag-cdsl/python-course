"""
Plus from Picture
https://codeforces.com/contest/1182/problem/B
"""

import itertools
import operator


h, w = [int(x) for x in input().split()]
data = [list(input()) for _ in range(h)]

FREE = '.'
OCCUPIED = '*'


class Column:
    def __init__(self, mat, col_idx):
        self._mat = mat
        self._col_idx = col_idx
    
    def __getitem__(self, i):
        return self._mat[i][self._col_idx]
    
    def __setitem__(self, i, item):
        self._mat[i][self._col_idx] = item
    
    def __len__(self):
        return len(self._mat)


def clear_ray(arr, origin_idx, to_right: bool):
    if to_right:
        delta = 1
        bound = len(arr)
        op = operator.lt
    else:
        delta = -1
        bound = 0
        op = operator.ge
        
    i = origin_idx + delta
    while op(i, bound) and arr[i] == OCCUPIED:
        arr[i] = FREE
        i += delta


shifts = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y = None, None
for i, j in itertools.product(range(1, h-1), range(1, w-1)):
    if data[i][j] == OCCUPIED and all(data[i + di][j + dj] == OCCUPIED
                                   for di, dj in shifts):
        data[i][j] = FREE
        clear_ray(data[i], j, to_right=False)
        clear_ray(data[i], j, to_right=True)
        clear_ray(Column(data, j), i, to_right=False)
        clear_ray(Column(data, j), i, to_right=True)
        
        for row in data:
            if OCCUPIED in row:
                print('NO')
                break
        else:
            print('YES')
        break
else:
    print('NO')
