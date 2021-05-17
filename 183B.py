# I didn't know how to solve this, so I looked at the editorial to get the formula.
x1, y1, x2, y2 = list(map(int, input().split()))
res = (x1 * y2 + x2 * y1)/(y1 + y2)
print(res)