v, t, s, d = map(int, input().split())
# distance = vt, if vt > d, it is a hit
print("Yes" if v * t > d or v * s < d else "No")
# I had to look at the editorial and added this part:
# or vs < d