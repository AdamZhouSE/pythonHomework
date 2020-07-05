import re

def judge():
    for i in range(n):
        for j in range(i+1,n):
            for k in range(1,n):
                for p in range(k+1,n):
                    if(k==i or k==j or p==i or p==j): continue
                    if(arr[i]+arr[j]==arr[k]+arr[p]):
                        print(i,j,k,p)
                        return 1
                    
    return 0

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    tmp=input()
    arr=re.findall(r'\d+',tmp)
    arr=list(map(int,arr))
    if(judge()==0):
        print("no pairs")
                        