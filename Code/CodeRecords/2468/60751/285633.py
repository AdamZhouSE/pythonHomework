num=int(input())
for i in range(num):
    N=int(input())
    A=input().split(" ")
    r=[]
    m=1
    for j in range(len(A)):
        if j==0:
            for k in range(1,len(A)):
                m*=int(A[k])
            r.append(m)
        else:
            new_=r[j-1]*int(A[j-1])//int(A[j])
            r.append(new_)
    for i in r:
        print(i,end=" ")
    print()