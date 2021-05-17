m, h = list(map(int, input().split()))

if not h % m:  # 0 is falsy, so not 0 will be True
    print("Yes")
else:
    print("No")
