n = int(input())

l1 = list(map(int, input().split()))
k1 = l1[0]
c1 = l1[1:]
l2 = list(map(int, input().split()))
k2 = l2[0]
c2 = l2[1:]

rounds = 0
times = 0
while k1 != 0 and k2 != 0:
    if c1[0] > c2[0]:
        c1.append(c2[0]); del c2[0]; c1.append(c1[0]); del c1[0]
        rounds += 1; k1 += 1; k2 -=1; times += 1
    else:
        c2.append(c1[0]); del c1[0]; c2.append(c2[0]); del c2[0]
        rounds += 1; k1 -= 1; k2 +=1; times += 1
    if times > 1000:
        print(-1)
        exit()

print(rounds, end=" ")
if k1 == 0:
    print(2)
else:
    print(1)
