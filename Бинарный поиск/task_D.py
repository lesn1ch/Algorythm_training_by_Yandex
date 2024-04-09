def count_height(words, wide):
    lines = 1
    remain_cells_in_line = wide - words[0]
    for i in range(1, len(words)):
        if remain_cells_in_line < 1 + words[i]:
            lines += 1
            remain_cells_in_line = wide - words[i]
        else:
            remain_cells_in_line -= 1 + words[i]
    return lines

width, n1, n2= map(int, input().split())
words1 = list(map(int, input().split()))
words2 = list(map(int, input().split()))

ans = float('inf')
l = max(words1)
r = width - max(words2)

while l <= r:
    mid = (r + l) // 2
    right_part_width = width - mid
    h1 = count_height(words1, mid)
    h2 = count_height(words2, width - mid)
    if h1 < h2:
        ans = min(ans, h2)
        r = mid - 1
    else:
        ans = min(ans, h1)
        l = mid + 1
print(ans)