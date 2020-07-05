n=int(input())
strings=[]
for i in range(0,n):
    strings.append(input())
min_index=0
min_val=100000000
for i in range(0,n):
    if len(strings[i])<min_val:
        min_index=i
        min_val=len(strings[i])
s=strings[min_index]
sub=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        sub.append(s[i:j])
for i in range(0,len(sub)):
    for j in range(0,len(sub)-1):
        if(len(sub[j])<len(sub[j+1])):
            temp=sub[j]
            sub[j]=sub[j+1]
            sub[j+1]=temp
for i in sub:
    isfix=False
    for j in range(0,len(strings)):
        if i not in strings[j]:
            break
        if(j==len(strings)-1):
            isfix=True
    if isfix:
        print(len(i))
        break