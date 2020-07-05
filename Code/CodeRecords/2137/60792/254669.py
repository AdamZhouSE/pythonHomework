def isPerfectNum(n):
    list1=[]
    i=1
    while i<n:
        if(n%i==0):
            list1.append(i)
        i=i+1
    sum=0
    for i in range(0,len(list1)):
        sum=sum+list1[i]
    if sum==n:
        return True
    else:
        return False
    
n=int(input())
print(isPerfectNum(n))