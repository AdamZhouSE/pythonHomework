n=int(input())
ai,pi=[],[]
while n>0:
    n -= 1
    temp=input().split()
    ai.append(int(temp[0]))
    pi.append(int(temp[1]))
lowest=pi[0]
money=ai[0]*pi[0]
for i in range(1,len(pi)):
    if pi[i]>=lowest:
        money += ai[i]*lowest
    else:
        lowest=pi[i]
        money += ai[i]*lowest
print(money)