n,k=map(int,input().split(" "))
mat=[]
def choose(n,start,end):
    if n==1:
        result=[]
        for i in range(start,end+1):
            result.append([i])
        return result
    else:
        result=[]
        for j in range(start,end-n+2):
            temp=choose(n-1,j+1,end)
            for item in temp:
                temp1=[j]
                for it in item:
                    temp1.append(it)
                result.append(temp1)
        return result
for i in range(0,k):
    temp=list(map(int,input().split(" ")))
    mat.append(temp)
leng=1
jud=True
for l in range(n,0,-1):
    result=choose(l,0,n-1)
    for item in result:
        norm=[]
        for j in item:
            norm.append(mat[0][j])
        jud=True
        for nums in mat:
            ind=-1
            for it in norm:
                if it in nums:
                    if nums.index(it)>ind:
                        ind=nums.index(it)
                    else:
                        jud=False
                        break
                else:
                    jud=False
                    break
        if jud:
            break
    if jud:
        leng=l
        break
print(leng)