n, x = list(map(int, input().split()))
l = map(str, filter(lambda i: i != x, list(map(int, input().split()))))
print(" ".join(l))
# I wasn't expecting this to work in one try