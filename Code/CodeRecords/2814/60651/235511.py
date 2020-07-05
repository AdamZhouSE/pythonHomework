n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
su=0
for i in range(n):
    if i==0:
        su+=1
    else:
        if list1[i]>=sum(list1[0:i]):
            su+=1
        else:
            list1[i]=0
print(su)        
        
        