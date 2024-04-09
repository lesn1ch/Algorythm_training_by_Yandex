n, k = map(int, input().split())
flag = False
nums = list(map(int, input().split()))
pos_dict = {}

for i in range(n):
    if nums[i] in pos_dict:
        if i - pos_dict[nums[i]] > k:
            pos_dict[nums[i]] = i
        else:
            flag = True
            break
    else:
        pos_dict[nums[i]] = i

if flag:
    print('YES')
else:
    print('NO')