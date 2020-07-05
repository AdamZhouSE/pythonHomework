def mat_FindKth():
    n=int(input())
    mat=[]
    for i in range(0,n):
        mat.append(eval("["+input()+"]"))
    K=int(input())
    l=mat[0][0]
    r=mat[len(mat)-1][len(mat)-1]
    while l<r:
        mid=(l+r)//2
        count=0

        for j in range(0,len(mat)):
            i=0
            while i<=len(mat)-1:
                if mid>=mat[len(mat)-1-i][j]:
                    count+=len(mat)-i
                    break
                else:
                    i+=1
        if count>=K:
            r=mid
        else:
            l=mid+1

    print(l)

if __name__=='__main__':
    mat_FindKth()