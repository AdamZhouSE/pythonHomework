n=int(input())
for i in range(0,n):
    s=list(input())
    j=1
    while j!=len(s):
        if(s[j]==s[j-1]):
            s.pop(j)
            j-=1
        j+=1
    for i in s:
        print(i,end="")
    print()