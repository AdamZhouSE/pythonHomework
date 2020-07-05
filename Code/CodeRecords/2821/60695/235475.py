n = int(input())
p = input().split(" ")
for i in range(0, n):
    p[i] = int(p[i])
playerS = 0
playerD = 0
head = 0
tail = n-1
if n == 1:
    playerS = p[0]
else:
    while head <= tail:
        if p[head] >= p[tail]:
            playerS += p[head]
            head += 1
            if head > tail:
                break
            if p[head] >= p[tail]:
                playerD += p[head]
                head += 1
            else:
                playerD += p[tail]
                tail -= 1
        else:
            playerS += p[tail]
            tail -= 1
            if head > tail:
                break
            if p[head] >= p[tail]:
                playerD += p[head]
                head += 1
            else:
                playerD += p[tail]
                tail -= 1


print(str(playerS)+" "+str(playerD))