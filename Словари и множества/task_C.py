n =int(input())
nums = list(map(int, input().split()))
nums_set = set(nums)
pos_dict = {}
neg_dict = {0: 0}
for num in nums:
    pos_dict[num] = pos_dict.get(num, 0) + 1
    if num + 1 in nums_set:
        neg_dict[num + 1] = neg_dict.get(num + 1, 0) + 1
    if num - 1 in nums_set:
        pos_dict[num-1] = pos_dict.get(num - 1, 0) + 1

print(min(n - pos_dict[max(pos_dict, key=pos_dict.get)], n - neg_dict[max(neg_dict, key=neg_dict.get)]))