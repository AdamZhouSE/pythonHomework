def arrange(row,start,sum):
    size=len(row)
    if(start==size-2):
        return sum
    target=1+row[start]//2*2-row[start]%2
    if(target==row[start+1]):
        return arrange(row,start+2,sum)
    for i in range(start+2,size):
        if(row[i]==target):
            row[i]=row[start+1]
            row[start+1]=target
            return arrange(row,start+2,sum+1)
        
row=eval(input())
res=arrange(row,0,0)
print(res)