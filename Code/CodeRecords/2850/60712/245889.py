n = int(input())
list1 = list(map(int,input().split()))
max1 = 0
maxtemp = 0
for i in range(n):
    if list1[i] ==1:
        max1=max1+1
for i in range(n-1):
    temp = 0
    for j in range(i,n):
        if list1[j] ==0:
            temp +=1
        else:
            temp -=1
        if maxtemp<temp:
            maxtemp=temp
print(max1+maxtemp)                    
