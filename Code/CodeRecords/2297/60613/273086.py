NUM=int(input())
lst=list(map(int,input().split()))
height=int(input())
i=pow(2,(height-1))-1
result=[]
if i>len(lst):
    print("EMPTY")
else:
    while i<len(lst):
        if(i<pow(2,(height-1))-1+pow(2,height-1)):
            result.append(lst[i])
            i+=1
        else:
            break
    for i in range(0,len(result)-1):
        print(result[i],end=" ")
    print(result[len(result)-1])

# 表示仍然有问题