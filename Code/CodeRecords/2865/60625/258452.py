numberOfUdesks=int(input())
large=int(input())
Udesks=[]
for i in range(numberOfUdesks):
    Udesks.append(int(input()))
Udesks.sort(reverse=True)
sumOfLarge=0
usedUdesks=0

for l in Udesks:
    if large>sumOfLarge:
        sumOfLarge+=l
        usedUdesks+=1
print(usedUdesks)