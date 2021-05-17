n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = []

for i in range(1,n):
    l += filter(lambda x: a[x] <= i <= b[x], range(n))

l = list(filter(lambda x: x != 0, l))
print(l)