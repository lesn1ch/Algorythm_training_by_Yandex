K = int(input())
X = []
Y = []
for _ in range(K):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
print(min(X), min(Y), max(X), max(Y))