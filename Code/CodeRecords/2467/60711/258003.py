import re
sea=re.compile(r'\d+')

def find(total,M,N):
    M=sea.findall(M)
    N=sea.findall(N)
    m=0
    n=0
    target=0
    for x in range(int(total[4])):
        if int(M[m])<=int(N[n]):
            target=int(M[m])
            m+=1
        else:
            target=int(N[n])
            n+=1
    print(target)
    if target==1:
        print(total,':',M,':',N)
    return

num=int(input())
for i in range(num):
    find(input(),input(),input())