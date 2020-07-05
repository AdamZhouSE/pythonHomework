temp=input().split()
n=int(temp[0])
k=int(temp[1])

strs=[]

for i in range(k):
    temp=input().split()
    strs.append(temp)

def common(a,b):
    res=''
    start=0
    for i in range(len(a)):
        for j in range(start,len(b)):
            if(i<len(a) and j<len(b)):
                if(a[i]==b[j]):
                    res+=a[i]
                    start=j+1
                    i+=1
    return res

res=''

for i in range(k):
    if(i==0):   
        res=common(strs[i],strs[i+1])
    else:
        res=common(res,strs[i])
               
print(len(res))
