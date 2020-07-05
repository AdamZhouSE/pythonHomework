A=eval(input())
k=int(input())
mid=list()
hel=dict()
for a in range(0,len(A)-1):
    for b in range(a+1,len(A)):
        value='['+str(A[a])+', '+str(A[b])+']'
        key=str(A[a]/A[b])
        hel[key]=value
        mid.append(A[a]/A[b])
mid.sort()
ind=str(mid[k-1])
print(hel[ind])

    