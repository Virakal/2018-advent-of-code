def try_combo(x, y):
    x = x.strip()
    y = y.strip()

    diff = 0
    common = []

    for i in range(len(x)):
        if x[i] == y[i]:
            common += x[i]
        else:
            diff += 1

    if diff == 1:
        print(''.join(common))
        exit()

# Main
with open('2-1.txt', 'r') as f:
    lines = list(f)

for line1 in lines:
    for line2 in lines:
        try_combo(line1, line2)
