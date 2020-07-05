cnt=input()
cnt=list(map(int,cnt.split(' ')))
limit=input()
limit=list(map(int,limit.split(' ')))
listA=input()
listA=list(map(int,listA.split(' ')))
listB=input()
listB=list(map(int,listB.split(' ')))
if(listA[limit[0]-1]<listB[len(listB)-limit[1]]):
    print("YES")
else:
    print("NO")
