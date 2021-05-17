# I had to read the editorial for this solution and slightly edited it

a, b, w = map(int, input().split())
upper = int((1000*w/a)//1)
lower = int(-(-((1000*w/b)//1)))
print("UNSATISFIABLE" if lower > upper else lower + " " + upper)
