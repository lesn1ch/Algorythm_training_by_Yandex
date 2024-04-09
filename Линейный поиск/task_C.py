n = int(input())
ropes = list(map(int, input().split()))
max_rope = ropes[0]
sum = 0
for i in range(1, n):
    sum += ropes[i]
    if ropes[i] > max_rope:
        sum = sum + max_rope - ropes[i]
        max_rope = ropes[i]

if sum >= max_rope:
    print((sum + max_rope))
else:
    print(max_rope - sum)