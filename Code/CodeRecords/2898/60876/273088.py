n=int(input())
l=list(input())
sum1=0
sum0=0
for item in l:
    if item=='1':
        sum1+=1
    else:
        sum0+=1
s='1'+'0'*sum0
print(s,end="")