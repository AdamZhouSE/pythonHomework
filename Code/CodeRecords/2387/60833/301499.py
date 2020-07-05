numlist=list(map(int,input().split(' ')))
count=numlist[0]
n=numlist[1]
numlist1=list(map(int,input().split(' ')))
for i in range(0,n):
    numlist = list(map(int, input().split(' ')))
    judge=False
    if numlist[0]:
        judge=True
    left=numlist[1]
    right=numlist[2]
    temp=numlist1[left-1:right]
    temp.sort(reverse=judge)
    for j in temp:
        numlist1[left-1]=j
        left+=1
print(numlist1[int(input())-1])