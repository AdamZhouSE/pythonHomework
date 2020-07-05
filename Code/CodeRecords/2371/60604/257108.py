n=int(input())
for I in range(n):
    s=input()
    #print(s)
    tmp=[]
    for i in s:
        if i.isalpha():
            tmp.append(i.lower())
    #print(tmp)
    res=True
    for i in range(len(tmp)):
        if tmp[i]!=tmp[-(i+1)]:
            res=False
    if res:
        print("YES")
    else:
        print("NO")