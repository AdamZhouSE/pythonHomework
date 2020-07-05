def ba(A):
    n=len(A)
    cnt1=sum(A)
    if cnt1%3!=0:
        print(list([-1,-1]))
        return
    if cnt1==0:
        print(list([0,2]))
        return
    cnt1//=3
    cnt=0
    l,r=[0]*3,[0]*3
    for i in range(n):
        if A[i]==0:
            continue
        cnt+=1
        if (cnt-1)%cnt1==0:
            l[(cnt-1)//cnt1]=i
        if cnt%cnt1==0:
            r[(cnt-1)//cnt1]=i
    for i in range(3):
        r[i]+=n-1-r[2]
    if A[l[1]:r[1]+1]!=A[l[0]:r[0]+1] or A[l[2]:r[2]+1]!=A[l[0]:r[0]+1]:
        print(list([-1,-1]))
        return
    print(list([r[0],r[1]+1]))
if __name__ == '__main__':
    ba([int(i) for i in input().split(',')])
