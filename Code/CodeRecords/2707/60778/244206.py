def arrange(row,start):
    size=len(row)
    if(start==size-2):
        return 0
    target=1+row[start]//2*2-row[start]%2
    if(target==row[start+1]):
        return 0+arrange(row,start+2)
    for i in range(start+2,size):
        if(row[i]==target):
            row[i]=row[start+1]
            row[start+1]=target
            ar=arrange(row,start+1)
            return 1+ar
        
row=eval(input())
res=arrange(row,0)
print(res)