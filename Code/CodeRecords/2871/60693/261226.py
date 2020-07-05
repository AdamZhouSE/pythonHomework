def make_3_team(arr):
    numof1,numof2=0,0
    for x in arr:
        if x==1:numof1+=1
        if x==2:numof2+=1
    if numof2>=numof1:
        return numof1
    if numof2<numof1:
        return numof2+(numof1-numof2)//3

n=int(input())
arr=list(map(int,input().split()))
print(make_3_team(arr))