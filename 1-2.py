with open('1-1.txt', 'r') as f:
    lines = list(f)

hit = {}
a = 0

while True:
    for line in lines:
        hit[a] = True

        a += int(line)

        if a in hit:
            print(a)
            exit()
