def judge(x,y):
    listx=x.split()
    listy=y.split()
    if len(listx)<len(listy):
        min=len(listx)
    else:
        min=len(listy)
    for i in range(0,min):
        if listx[i]>listy[i]:
            return 1
        else:
            if listx[i]<listy[i]:
                return 0
    if len(listx)>=len(listy):
        return 0
    else:
        return 1

n=input()
list=input().split(" ")

while True:
    max = list[0]
    for i in range(0,int(n)-1):
        if not(judge(list[i],list[i+1])):
            max=list[i+1]
    print(max, end="")
    list.remove(max)
    n=int(n)-1
    if n==1:
        break