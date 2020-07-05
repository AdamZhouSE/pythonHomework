def insert(key,Hash):
    P=len(Hash)
    index=key%P
    tmp=index
    c=1
    # sign True-> + False-> -
    sign=True
    while Hash[tmp%P]!=-1:
        tmp=index
        if sign:
            tmp=index+c**2
            sign=False
        else:
            tmp=index-c**2
            c+=1
            sign=True
    return tmp


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
    Hash[a]=word
print(" ".join(str(i) for i in ans))