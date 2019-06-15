with open('data/1.txt', 'r') as f:
    lines = list(f)

result = sum(int(line) for line in lines)

print(result)
