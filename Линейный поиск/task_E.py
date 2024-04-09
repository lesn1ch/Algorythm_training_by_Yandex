from collections import deque
n = int(input())
good_ind = deque()
bad_ind = deque()
berries = []
last_boost = -1
last_down = -1
for i in range(1, n+1):
    up, down = map(int, input().split())
    berries.append((up, down))
    if up > down:
        if down > last_down:
            last_down = down
            good_ind.append(i)
        else:
            good_ind.appendleft(i)

    else:
        if last_boost < up:
            last_boost = up
            bad_ind.appendleft(i)
        else:
            bad_ind.append(i)

max_height = 0
total_h = 0
for i in good_ind + bad_ind:
    total_h += berries[i -1][0]
    if total_h > max_height:
        max_height = total_h
    total_h -= berries[i -1][1]

output = ' '.join(map(str, good_ind + bad_ind))

print(max_height)
print(output)
