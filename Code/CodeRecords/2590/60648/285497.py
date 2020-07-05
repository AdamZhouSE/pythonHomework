n=int(input())
for i in range(n):
    s=input()
    ls=[]
    for j in s:
        if j not in ls:
            ls.append(j)
    le=len(ls)
    if le%2==0:
        print("SHE!")
    else:
        print("HE!")