def insert(key,Hash):
    P=len(Hash)
    index=key%P
    c=1
    # sign True-> + False-> -
    sign=True
    while Hash[index]!=-1:
        if sign:
            index+=c**2
            sign=False
        else:
            index-=c**2
            c+=1
            sign=True
    return index


N, P = map(int, input().split())
s=list(input().split())
Hash=[-1]*P
ans=[]
for word in s:
    n=0
    index=2
    for i in range(len(word)-3,len(word)):
        n+=(ord(word[i])-65)*32**index
        index-=1
    a=insert(n,Hash)
    ans.append(a)
print(" ".join(str(i) for i in ans))