n=int(input())
s=input()
l=0
k=0
for i in range(n-1):
    if s[i]=='V' and s[i+1]=='K':
        l+=1
    if s[i]=='K' and s[i+1]=='K' and s[i-1]!='V' and k==0:
        l+=1
        k+=1
        i+=1
    if s[i]=='V' and s[i+1]=='V' and s[i-1]!='K' and k==0:
        l+=1
        k+=1
        i++1
print(l,end='')