change_set = set(input().split())
text = list(input().split())
text_w_changes = []

for word in text:
    change = ''
    for letter in word:
        change += letter
        if change in change_set:
            break
    text_w_changes.append(change)

print(*text_w_changes)