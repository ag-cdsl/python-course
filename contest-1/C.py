"""
Text Document Analysis
https://codeforces.com/contest/723/problem/B
"""

_ = input()
s = input()


def gen(s):
    n = len(s)
    word = []
    is_in_pars = False
    for i, c in enumerate(s):
        if c.isalpha():
            word.append(c)
            if i == n - 1 or not s[i + 1].isalpha():
                yield ''.join(word), is_in_pars
                word.clear()
        elif c == '(':
            is_in_pars = True
        elif c == ')':
            is_in_pars = False


max_len = 0
num_words = 0
for w, in_pars in gen(s):
    if in_pars:
        num_words += 1
    max_len = max(len(w), max_len)

print(max_len, num_words)
