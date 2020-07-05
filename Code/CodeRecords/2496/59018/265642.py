import math
def different(S):
    dict={}
    A=list(S)
    result=[]
    for i in A:                          #元素出现次数
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]=dict[i]+1
            
    if max(dict.values())<=math.ceil(len(A)/2):               #能错开
        info=[k for k,v in dict.items() if v==max(dict.values())]
        for j in range(len(A)-1,-1,-1):
            if A[j] in info:
                A.remove(A[j])
        A.sort()        
        for i in range(len(info)):        
            d=[]        
            d=d+[x for x in range(info[i],max(dict.values()))]
        for i in range(len(A)):
            result.append(d[0])
            result.append(A[i])
            while len(d)-1!=0:
                result.append(d[i])
                del d[i]
        inf=[str(x) for x in result]
        print(''.join(inf))
    else:
        print("")
            


S=input()
different(S)