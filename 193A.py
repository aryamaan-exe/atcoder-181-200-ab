a, b = list(map(int, input().split()))
print(((a - b) * 100) / a) # Decrease percent is calculated as: (change * 100) / initial value, where change = initial value - final value