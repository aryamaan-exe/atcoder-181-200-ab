# I had to look at the editorial for this problem
n = int(input())
a = list(map(int, input().split()))
 
ans = -1
mx = 0
 
for x in range(2, 1001):
	s = sum(i % x == 0 for i in a)
	if mx < s:
		mx = s
		ans = x
 
print(ans)