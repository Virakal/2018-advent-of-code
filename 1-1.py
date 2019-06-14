with open('1-1.txt', 'r') as f:
    lines = list(f)

lines = (int(x) for x in lines)
result = sum(line for line in lines)

print(result)
