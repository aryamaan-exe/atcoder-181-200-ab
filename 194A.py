a, b = list(map(int, input().split()))
c = a + b  # Total milk solids

if c >= 15 and b >= 8:
    print(1)
elif c >= 10 and b >= 3:
    print(2)
elif c >= 3:
    print(3)
else:
    print(4)
