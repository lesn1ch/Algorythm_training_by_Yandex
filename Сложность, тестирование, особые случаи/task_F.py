n = int(input())
nums = [int(i) for i in input().split()]
cnt = 0
pos_1 = -1
pos_2 = -1
i = 0
while i < (n - 1):
    if nums[i] % 2 == 0:
        if nums[i + 1] % 2 == 1:
            pos_2 = i
        i += 1
    else:
        cnt += 1
        if nums[i + 1] % 2 == 1:
            pos_1 = i
        else:
            pos_2 = i
        i += 1
if nums[n-1] % 2 == 1:
    cnt += 1
if cnt % 2 == 0:
    if pos_1 != -1:
        print(pos_1 * '+' + 'x' + (n - pos_1 - 1 - 1) * '+')
    else:
        print(pos_2 * '+' + 'x' + (n - pos_2 - 1 - 1) * '+')
else:
    print((n - 1) * '+')