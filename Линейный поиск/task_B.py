days, expiration = map(int, input().split())
prices = list(map(int, input().split()))
prices.append(-1)
max_profit = 0
for day in range(days):
    buy = prices[day]
    for pr in range(1, expiration + 1):
        if prices[day + pr] == -1:
            break
        max_profit = max(max_profit, prices[day + pr] - buy)

print(max_profit)