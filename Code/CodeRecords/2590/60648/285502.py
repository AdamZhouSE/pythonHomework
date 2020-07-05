n=int(input())
for i in range(n):
    s=input()
    #print(s)
    ls=[]
    for j in s:
        if j not in ls and j!='a' and j!='e' and j!='i' and j!='o' and j!='u':
            ls.append(j)
    le=len(ls)
    #print(le)
    if le%2==0:
        print("SHE!")
    else:
        print("HE!")