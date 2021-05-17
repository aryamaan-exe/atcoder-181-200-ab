s = input()
a = all(s[i].islower() for i in range(0, len(s), 2))
b = all(s[i].isupper() for i in range(1, len(s) - 1, 2))
print("Yes" if (a*b) else "No")
# I had to look at the editorial since I got 2 test cases wrong, however, I couldn't find why my answer was wrong.