"""
Page Numbers
https://codeforces.com/contest/34/problem/C
"""

nums = sorted({int(x) for x in input().split(',')})

out = []
was_in_interval = False
n = len(nums)

for i, num in enumerate(nums):
    if i != n - 1 and num + 1 == nums[i + 1]:
        if not was_in_interval:
            was_in_interval = True
            out.extend((num, '-'))
    else:
        was_in_interval = False
        out.extend((num, ','))

out = out[:-1]

print(''.join(str(x) for x in out))
