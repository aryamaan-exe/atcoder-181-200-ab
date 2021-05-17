'''
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

l = []
for i in range(n):
    l.append(sum(a[i]))

wa = list(map(lambda x: x[0], a))
wb = list(map(lambda x: x[1], a))
m1 = min(wa)
m2 = min(wb)
if wa.index(m1) != wb.index(m2):
    l.append(max(m1, m2))

print(min(l))
'''

# Above was my attempted solution, however I had to look at the editorial for this.

n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n) :
	a[i], b[i] = map(int, input().split())

res = 1000000000
for i in range(n) :
	for j in range(n) :
		res = min(res, a[i] + b[j] if i == j else max(a[i], b[j]))

print(res)