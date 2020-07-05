n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
initial_1 = list(s1)
initial_2 = list(s2)
r = 0
winner = -1
while len(s1) != 1 and len(s2) != 1:
    if s1[1] > s2[1]:
        s1.append(s2[1])
        s1.append(s1[1])
        s1.pop(1)
        s2.pop(1)
    else:
        s2.append(s1[1])
        s2.append(s2[1])
        s1.pop(1)
        s2.pop(1)
    if s1 == initial_1 and s2 == initial_2:
        break
    r += 1
if len(s1) == 1:
    print(r, 2)
elif len(s2) == 1:
    print(r, 1)
else:
    print(-1)