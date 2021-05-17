n = int(input())
a = []
indices = []
slopes = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        if i != j:
            indices.append([i, j])
# If n = 3, indices = [[0,1],[0,2],[1,2]]

for j in range(len(indices)):
    x1 = a[indices[j][0]][0]
    x2 = a[indices[j][1]][0]

    y1 = a[indices[j][0]][1]
    y2 = a[indices[j][1]][1]

    slope = (y2 - y1)/(x2 - x1) # Since slope = tan(theta), we use the formula of tan(theta)
    slopes.append(slope)

slopes = list(filter(lambda x: (x >= -1)*(x <= 1), slopes))
print(len(slopes))