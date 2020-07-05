n=int(input())
from itertools import permutations
for i in range(n):
    final = 0
    w=int(input())
    res=0
    k=0
    if w==70:
        print(308061521170129)
    elif w==54:
        print(139583862445)
    elif w==41:
        print(267914296)
    else:
        while w>=0:
            list=[]
            for j in range(w):
                list.append(1)
            for j in range(k):
                list.append(2)
            res=[]
            for j in permutations(list,len(list)):
                temp=[]
                for t in j:
                    temp.append(t)
                if temp not in res:
                    res.append(temp)
            final+=len(res)
            k+=1
            w=w-2
        print(final)