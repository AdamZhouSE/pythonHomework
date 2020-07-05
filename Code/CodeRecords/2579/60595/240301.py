def Test():
    n=int(input())
    mat=[]
    for i in range(0,n):
        mat.append(eval("["+input()+"]"))
    k=int(input())
    if(n==0 or mat[0]==0):
        print(0)
    else:
        result=0
        for i in range(0,n):
            nums=mat[i]
            for j in range(1,len(nums)):
                singlenums=nums[j]
                if(singlenums<=k):
                    result=1
                mat[i][j]=mat[i][j]+nums[j-1]
        if(result==0):
            print(0)
        else:
            for i in range(0,n):
                for j in range(0,len(mat[i])):
                    tes=get(mat,i,j,k)
                    result=max(result,tes)
            print(result)


def get(mat,x,y,k):
    tempx=x
    tempy=y
    if(x==0 or y==0):
        if(y!=0):
            return (1 if(mat[x][y]-mat[x][y-1]<=k) else 0)
        else:
            return (1 if(mat[x][y]<=k) else 0)
    length=1
    x=x-1
    y=y-1
    while(x>=0 and y>=0):
        t=0
        for i in range(x,tempx+1):
            if(y!=0):
                t=t+mat[i][tempy]-mat[i][y-1]
            else:
                t=t+mat[i][tempy]
        x=x-1
        y=y-1
        if(t<=k):
            length=length+1
        else:
            break
    return length
if __name__ == "__main__":
    Test()

