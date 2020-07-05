s=input()
t=list(input())
temp1=''
temp2=''
for i in range(0,len(s)):
    x=str(i)
    for j in range(0,len(t)):
        if t[j]==s[i]:
            t[j]=x
for j in range(0,len(t)):
    if t[j]>='0' and t[j]<='9':
        temp1=temp1+t[j]
    else:
        temp2=temp2+t[j]
temp=list(temp1)
for k in range(0,len(temp)-1):
    for m in range(k+1,len(temp)):
        if int(temp[m])<int(temp[k]):
            temp[m],temp[k]=temp[k],temp[m]
for p in range(0,len(s)):
    x=str(p)
    for q in range(0,len(temp)):
        if temp[q]==x:
            temp[q]=s[p]
result=temp2+''.join(temp)
print(result)