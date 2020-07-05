n=int(input())
ans=[]
for i in range(n):
    ans.append(i+1)
a_s=''
for i in range(len(ans)):
    a_s=a_s+str(ans[i])+' '
print(a_s,end='')