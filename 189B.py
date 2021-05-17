n, x = list(map(int, input().split()))
g = []
a = 0 # Let total intake be a.
y = '' # Let the output be y

for i in range(n):
    g.append(list(map(int, input().split())))

for i in range(n):
    ml = g[i][0]
    prc = g[i][1]
    a += ml * prc # I had to check the editorial since a few of my test cases were wrong. Our normal condition is ml * prc / 100 > x. But we can multiply both sides by 100 to get integer values. ml * prc > 100 * x
    if a > 100 * x:
        y = i+1
        break

print(-1 if y == '' else y)