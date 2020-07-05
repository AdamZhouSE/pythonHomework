import re
T=int(input())
res=[]
for a in range(T):
    inp=input()
    num=re.sub(r"6","9",inp)
    num=int(num)
    res.append(str(num-int(inp)))
for i in res:
    print(i)