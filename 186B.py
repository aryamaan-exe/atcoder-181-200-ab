h, w = list(map(int, input().split()))
a = []
for i in range(h):
    a += list(map(int, input().split()))

m = min(a)
x = 0
for j in range(h*w):
    if a[j] != m:
        x += a[j] - m

print(x)