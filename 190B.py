n, s, d = list(map(int, input().split()))
spells = []
_ = False
for i in range(n):
    spells.append(list(map(int, input().split())))

for spell in spells:
    if spell[0] < s:
        if spell[1] > d:
            _ = True
            break

print("Yes" if _ else "No")