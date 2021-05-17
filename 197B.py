h, w, x, y = list(map(int, input().split()))
table = []
res = 0

for _ in range(h):
    table.append(list(input()))

for i in range(x, h):
    if table[i][y] != "#":
        res += 1

for i in range(x, 0, -1):
    if table[i][y] != "#":
        res += 1


for j in range(y, w+1):
    if table[x][j] != "#":
        res += 1

for j in range(y, 0, -1):
    if table[x][j] != "#":
        res += 1

print(res)

# I had to look at the editorial for this, so I converted the C++ code they gave to Python.

'''
for (int i = x; i < h && s[i][y] != '#'; i++) cnt++;
for (int i = x; i >= 0 && s[i][y] != '#'; i--) cnt++;
for (int j = y; j < w && s[x][j] != '#'; j++) cnt++;
for (int j = y; j >= 0 && s[x][j] != '#'; j--) cnt++;
'''
