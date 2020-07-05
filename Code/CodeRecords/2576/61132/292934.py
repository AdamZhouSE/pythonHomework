arr=list(map(int,input().split(',')))
target=int(input())
l=len(arr)
value=target//l
Min=target-sum([i if i<=value else value for i in arr])
while True:
    value+=1
    tmp=abs(target-sum([i if i<=value else value for i in arr]))
    if Min>tmp:
        Min=tmp
    else:
        print(value-1)
        break