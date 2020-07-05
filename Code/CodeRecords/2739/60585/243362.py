def recursiveFind(count,number,temp,re):
    for i in range(number,10):
        if re<i:
            break
        recursiveFind(count+1,i+1,temp+[i],re-i)
    if count==k:
        if re==0:
            result.append(temp)
    return
num=input().split(', ')
k=int(num[0])
n=int(num[1])
result=[]
temp=[]
recursiveFind(0,1,temp,n)
print(result)