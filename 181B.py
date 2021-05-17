n = int(input())
l = []
sum = 0

for _ in range(n):
    l.append(list(map(int, input().split())))

# While I was stuck doing nested for loops, I remembered a story I saw on youtube about Carl F Gauss. His teacher told
# the whole class to find 1 + 2 + 3... all the way to 100. While his students kept adding, Gauss arrived at the answer
# in no time. He said that 1 + 100 = 101, 2 + 99 = 101, and so on. He halved 100 (since he paired them) and multiplied
# 50 and 101 to get 5050.

for i in range(len(l)):
    # I kept getting a few test cases wrong. Since I couldn't see those cases, I suspected that they might have not given the numbers in order.
    l[i].sort()
    a = l[i][0]
    b = l[i][1]
    # x = the sum of the two nos. on the extreme
    x = a + b
    c = (b - a) + 1  # c is how many numbers are between a and b
    if c < 0:
        c *= -1  # Small bug, if nos. are negative, convert c to positive.

    sum += (x * (c // 2)) + ((a + b) / 2 if c %
                             2 == 1 else 0)  # If c is divisible by 2

    # For example, we take 10 + 11 + 12 + 13. a = 10, b = 13, x = 23, c = 4. Since (13 - 10) % 2 or 3 % 2 == 1,
    # sum becomes 23 * 2 = 46

sum = int(sum)
print(sum)

# Although this logic adds a bit of complexity, it reduces the time taken since it is faster than a for loop.
