def permuate(src,start,end,res):
    if start== end:
        res.append(''.join(src))
    else:
        for i in range(start,end+1):
            src[start],src[i]=src[i],src[start]
            permuate(src,start+1,end,res)
            src[start], src[i] = src[i], src[start]


n = int(input())
k =int(input())
src=[str(x) for x in range(1,n+1)]
repo=[]
permuate(src,0,len(src)-1,repo)
print(repo[k-1])
