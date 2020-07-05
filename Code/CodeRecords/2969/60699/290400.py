s=input()
s=" "+s
N=len(s)-1
i=1
while i<=N:
    j=i
    k=i+1
    while j<=N and k<=N and s[j] <=s[k]:
        if s[j]<s[k]:
            j=i
        else:
            j+=1
        k+=1
    while i<=j:
        if i+(k-j)>N:
            print(i+k-j-1)
        else:
            print(i+k-j-1,end=' ')
        i+=(k-j)