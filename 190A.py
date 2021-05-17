l = list(map(int, input().split()))
a, b, c = l
turn = None

if c == 0:
    turn = "T"
else:
    turn = "A"

# Since I got a few test cases wrong, it could be that they expect the reverse output in case both have 0 candies
if [0, 0] == [a, b]:
    if c == 0:
        print("Aoki")
    else:
        print("Takahashi")
else:
    while True:
        if turn == "T":
            a -= 1
            turn = "A"
            if b == 0:
                print("Takahashi")
                break
        if turn == "A":
            b -= 1
            turn = "T"
            if a == 0:
                print("Aoki")
                break