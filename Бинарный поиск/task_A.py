def lbinsearch(nums, x):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] >= x:
            r = m - 1
        else:
            l = m + 1
    return l

def rbinsearch(nums, x):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] > x:
            r = m - 1
        else:
            l = m + 1
    return r

n = int(input())
nums = sorted(list(map(int, input().split())))
k = int(input())
res = []
for _ in range(k):
    left, right = map(int, input().split())
    res.append(rbinsearch(nums, right) - lbinsearch(nums, left) + 1)

print(*res)
