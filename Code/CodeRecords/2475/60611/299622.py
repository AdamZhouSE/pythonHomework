num=int(input())
for i in range(num):
    n=int(input())
    t=sorted(list(map(int,input().split(" "))))
    maximum=0
    count=1
    for j in range(1,len(t)):
        if t[j]==t[j-1]+1:
            count+=1
            if count>maximum:maximum=count
        else:
            count=1
    print(maximum)