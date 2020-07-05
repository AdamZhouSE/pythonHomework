def height(n):
    i=1
    ans=-1
    while(n>=0):
        n=n-i
        i=i*2
        ans+=1
    return ans
tree=list(map(str,input()[1:-1].split(",")))
minid=tree.index("null")
print(height(minid))