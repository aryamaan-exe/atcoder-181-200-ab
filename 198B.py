n = int(input())
x = list(str(n))
y = ""

# The following 2 loops strip the 0s off of the start and end, while still keeping the ones in the middle.
if "0" in x:
    for i in range(len(x)):
        if x[i] != "0":
            y = x[i:]
            break
    for j in range(len(y)):
        if y[~j] != "0" and j != 0:
            x = y[:-j]
            break

x = int("".join(x))
if n == int(str(n)[::-1]): print("Yes")
elif x == int(str(n)[::-1]): print("Yes")
else: print("No")

# l[::-1] = l.reverse()