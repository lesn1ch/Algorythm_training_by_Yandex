w1 = dict()
for letter in input():
    w1[letter] = w1.get(letter, 0) + 1

w2 = dict()
for letter in input():
    w2[letter] = w2.get(letter, 0) + 1

if w1 == w2:
    print('YES')
else:
    print('NO')