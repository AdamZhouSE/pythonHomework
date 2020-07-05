import sys
import re
import math
s=sys.stdin.read()
slist=s.split('\n')
n=int(slist[0])
del(slist[0])
express=[]
for i in range(n):
    command=slist[i]
    if command[0]=='A':
        digits=re.findall(r"-?\d+",command)
        nums= [int(e) for e in digits ]
        express.append(nums)
    elif command[0]=='Q':
        digits=re.findall(r"-?\d+",command)
        nums= [int(e) for e in digits ]
        k=nums[0]
        ans=0
        if len(express)==0:
            print(0)
        else:
            for exp in express:
                a=exp[0]
                b=exp[1]
                c=exp[2]
                if a*k+b>c:
                    ans+=1
            print(ans)
    else:
        digits=re.findall(r"-?\d+",command)
        nums= [int(e) for e in digits ]
        k=nums[0]
        if len(express)>=1 and k-1<len(express):
            del(express[k-1])
        else:
            del(express[0])
        
            
    