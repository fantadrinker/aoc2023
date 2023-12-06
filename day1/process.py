f = open("data.txt", "r")
# print(f.read())
i = 0
for line in f:
    i += 1
    print(f'{i}: {line}')
