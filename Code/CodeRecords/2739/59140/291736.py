def search(n,k,start,last,s):
    if start>last:
        if len(s)==k:
            sum=0
            numlist=[]
            for i in list(s):
                sum+=int(i)
                numlist.append(int(i))
            if sum==n:result.append(numlist)
    else:
        search(n,k,start+1,last,s+str(start))
        search(n, k, start + 1, last, s)

temp=input().split(",")
k=int(temp[0])
n=int(temp[1])
result=[]
search(n,k,1,9,"")
print(result)
