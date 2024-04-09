n, m = map(int, input().split())
army = list(map(int, input().split()))
prefix_sum = [0]
sum = 0
for i in range(n):
    sum += army[i]
    prefix_sum.append(sum)
ans = []
for _ in range(1, m + 1):
    num_teams, num_ork = map(int, input().split())
    l = 0
    r = n - num_teams
    mid = (l + r) // 2
    while l <= r:
        if prefix_sum[mid + num_teams] - prefix_sum[mid] > num_ork:
            r = mid - 1
        else:
            l = mid + 1
        mid = (l + r) // 2
    if prefix_sum[mid + num_teams] - prefix_sum[mid] == num_ork:
        ans.append(mid+1)
    elif l > r:
        ans.append(-1)
    else:
        ans.append(l + 1)

print(*ans, sep='\n')