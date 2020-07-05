n=int(input())
list1=input().split()
list1=list(map(int,list1))
list1.sort()
i=1
sum1=list1[0]
count=n
while(True):
    if(i<count):
        if(list1[i]>=sum1):
            sum1=list1[i]+sum1
            i=i+1
        else:
            del list1[i]
            count=count-1
    else:
        break
print(len(list1))
            