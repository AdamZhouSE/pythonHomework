n=int(input())
coms=input().split(' ')
coms=[int(x) for x in coms]
i=1;days=0
coms.sort()
while True:
    enough=False
    for j in range(len(coms)):
        if coms[j]>=i:
            del coms[j]
            days+=1
            i+=1
            coms.sort()
            enough=True
            break
    if not enough or days==n:
        break
print(days)