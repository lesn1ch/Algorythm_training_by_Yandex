team1_g1, team2_g1 = (int(i) for i in input().split(sep=':'))
team1_g2, team2_g2 = (int(i) for i in input().split(sep=':'))
loc = int(input())

if team1_g1 + team1_g2 > team2_g1 + team2_g2:
    print(0)
else:
    need = team2_g1 + team2_g2 - (team1_g1 + team1_g2)
    if ((need + team1_g2 > team2_g1) and loc == 1) or (team1_g1 > team2_g2 and loc == 2):
        print(need)
    else:
        print(need + 1)