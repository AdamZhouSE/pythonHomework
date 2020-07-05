t=int(input())
for i in range(t):
    s=list(input())
    a=[1 for j in range(len(s))]
    answer=0
    for j in range(len(s)):
        s[j]=ord(s[j])-96
    for j in range(len(s)):
        for k in range(j):
            if(s[k]<s[j]):
                a[j]=max(a[j],a[k]+1)
                answer=max(answer,a[j])
    print(answer)