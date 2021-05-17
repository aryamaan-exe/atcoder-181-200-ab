n, x = list(map(int, input().split()))
s = input()

for i in range(n):
    if s[i] == "x":
        x += 1
    else:
        x -= 1 if x != 0 else 0

print(x)
