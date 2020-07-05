str1=input().split(' ')
m=int(str1[0])
n=int(str1[1])
a=input()
b=input()
ans=[]
for i in range(n-m+1):
    flag=1
    p=0
    for j in range(i,i+m):
        if a[p]!=b[j] and a[p]!='*' and b[j]!='*':
            flag=0
        p=p+1
    if flag==1:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    ans[i]=ans[i]+1
a_s=''
for i in range(len(ans)):
    a_s=a_s+str(ans[i])+' '
print(a_s)
    
            
    