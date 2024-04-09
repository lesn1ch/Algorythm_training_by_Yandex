res = 0

n = int(input())
for i in range(n):
    num_spaces = int(input())
    if num_spaces != 0:
        res += num_spaces // 4
        if num_spaces % 4 == 1:
            res += 1
        else :
            res += 2 * ((num_spaces % 4) // 2)

print(res)