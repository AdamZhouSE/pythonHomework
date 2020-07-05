A=input()
new=[]
nn=len(A)
for i in range(nn):
    if A[i].isdecimal():
        new.append(int(A[i]))
def minimum(N):
    n=len(N)
    t=0
    result=0
    for k in range(n):
        i=t
        if new[i]%2==0:
            if new[i+1]==new[i]+1:
                if t<n-2:
                    t=t+2
            else:
                for j in range(i+1,n):
                    if new[j]==new[i]+1:
                        a=new[i+1]
                        new[i+1]=new[j]
                        new[j]=a
                        result=result+1
        else:
            if new[i+1]==new[i]-1:
                if t<n-2:
                    t=t+2
            else:
                for j in range(i+1,n):
                    if new[j]==new[i]-1:
                        a=new[i+1]
                        new[i+1]=new[j]
                        new[j]=a
                        result=result+1
        if t==n-2:
            break
    print(result)
    return 0
minimum(new)