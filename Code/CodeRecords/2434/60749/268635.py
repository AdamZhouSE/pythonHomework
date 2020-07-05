str1=input().split(" ")
n=int(str1[0])
m=int(str1[1])
c=int(str1[2])
num_array=list(map(int,input().split(" ")))
def findlocation(n,m,c,nums):
    res=[]
    for t in range(n-m+1):
        temp=nums[t:t+m]
        minus=max(h for h in temp)-min(h for h in temp)
        if minus <=c:
            res.append(t)
    return res
res=findlocation(n,m,c,num_array)
if len(res)==0:
    print("NONE")
else:
    for h in res:
        print(str(h+1))