n, k, d = (int(i) for i in input().split())
is_changed = False
for i in range(10):
    if (n * 10 + i) % k == 0:
        is_changed = True
        n = n * 10 + i
        break
if is_changed == True:
    print(str(n) + '0'*(d-1))
else: print(-1)