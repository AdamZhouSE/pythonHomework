NUM=int(input())
lst=list(map(int,input().split()))

if len(lst)<3:
    print(0)
elif  len(lst)==3:
    if lst[0]<lst[1] and lst[1] <lst[2]:
        print(1)
    else:
        print(0)
else:
    result=0
    for i in range(len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                if lst[i] <lst[j] and lst[j] <lst[k]:
                    result+=1
    print(result,end="")

