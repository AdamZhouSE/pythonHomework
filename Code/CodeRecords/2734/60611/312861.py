from collections import defaultdict

n,c,m=list(map(int,input().split(" ")))
ns=list(map(int,input().split(" ")))
for i in range(m):
    begin,end=list(map(int,input().split(" ")))
    begin-=1
    s=defaultdict(lambda :0)
    new_array=ns[begin:end:]
    for k in new_array:
        s[k]+=1
    result=0
    for k in set(new_array):
        if s[k]>=2:
            result+=1
    print(result)
