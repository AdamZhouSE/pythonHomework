A=eval(input())

def fourSumCount( A):
    jfk=[]
    for i in range(len(A)):
        if A[i][0]=='JFK':
            jfk.append((A[i][1],i))
    dic=dict(jfk)
    want=sorted(dic)
    start=dic[want[0]]
    ori=A[start][1]
    del A[start]
    cons=['JFK',ori]
    mark=1
    while mark!=0:
        c=0
        for i in range(len(A)):
            if A[i][0]==ori:
                cons.append(A[i][1])
                c=1
                ori=A[i][1]
                del A[i]
                break
        if c==1:
            mark=1
        else:
            mark=0
    return cons
print(fourSumCount(A))