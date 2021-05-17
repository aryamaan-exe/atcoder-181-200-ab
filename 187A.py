a = list(input().split())
s = []
for i in a:
    sum = 0
    for j in i:
        x = int(j)
        sum += x
    s.append(sum)

print(max(s))
