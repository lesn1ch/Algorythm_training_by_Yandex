my_dict = {}
res = set()
for i in range(3):
    n = int(input())
    nums = set(map(int, input().split()))
    for num in nums:
        if num in my_dict:
            res.add(num)
        else:
            my_dict[num] = 1

print(*sorted(res))