a = list(map(int, input().split()))
a.sort()

if a[1] - a[0] < 3:
    print("Yes")
else:
    print("No")