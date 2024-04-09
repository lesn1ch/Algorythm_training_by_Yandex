n = int(input())
desk = [list('-'*10)]
for line in range(8):
    desk.append(['-'] + [0]*10 + ['-'])
desk.append(list('-'*10))

for cell in range(n):
    i, j = map(int, input().split())
    desk[i][j] = 1
p = 0
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for i in range(1, 10):
    for j in range(1, 10):
        if desk[i][j] == 1:
            neighbours = 0
            for k in range(len(di)):
                if desk[i + di[k]][j + dj[k]] == 1:
                    neighbours += 1
            p = p + (4 - neighbours)

print(p)