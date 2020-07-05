inlist=list(input())
n=len(inlist)
sum=0
for i in range(n-2):
    if inlist[i]=='Q':
        for j in range(i+1,n-1):
            if inlist[j]=='A':
                for k in range(j+1,n):
                    if inlist[k]=='Q':
                        sum+=1
print(sum,end="")            
    
