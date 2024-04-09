n = int(input())
song_rate = dict()
ans = []
for _ in range(n):
    k = int(input())
    songs = set(input().split())
    for song in songs:
        song_rate[song] = song_rate.get(song, 0) + 1

for key, value in song_rate.items():
    if value == n:
        ans.append(key)

print(len(ans))
ans = ' '.join(map(str, sorted(ans)))
print(ans)