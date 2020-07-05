def cal(a):
    count=0    
    for i in range(len(a)-1):
        if a[i]=='V'and a[i+1]=='K':
            count+=1
    return count
def change(a,i):
    b=[0]*len(a)
    for j in range(i):
        b[j]=a[j]
    if a[i]=='K':
        b[i]='V'
        
    else:
        b[i]='K'
    for j in range(i+1,len(a)):
        b[j]=a[j]
    return b
n=input()
s=list(input())


max=cal(s)
for i in range(len(s)):
    tmp=change(s,i)
    if cal(tmp)>max:
        max=cal(tmp)
print(max,end="")