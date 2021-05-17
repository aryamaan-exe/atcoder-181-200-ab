n = int(input())
a = []
candidates = []

for i in range(n): a.append(list(map(int, input().split())))
for j in range(n):
    if a[j][2] - a[j][0] > 0:
        candidates.append(a[j][1])
try:
    print(min(candidates))
except:
    print(-1)