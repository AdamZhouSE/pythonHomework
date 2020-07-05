n=int(input())
list=list(map(int,input().split(" ")))
sum1=0
sum2=0
sum1_turn=True
for i in range(n):
    length=len(list)
    if sum1_turn:
        if list[length-1]>list[0]:
            sum1+=list[length-1]
            list.pop()
            sum1_turn=False
        else:
            list.reverse()
            sum1+=list[length-1]
            sum1_turn=False
            list.pop()
            list.reverse()
    else:
        if list[length-1]>list[0]:
            sum2+=list[length-1]
            list.pop()
            sum1_turn=True
        else:
            list.reverse()
            sum2+=list[length-1]
            sum1_turn=True
            list.pop()
            list.reverse()
print(f'{sum1}'+" "+f'{sum2}')        
    