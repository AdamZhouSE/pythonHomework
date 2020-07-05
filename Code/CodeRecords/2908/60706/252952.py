n=int(input())
eng=[]
for i in range(n):
    list4=list(input())
    count=len(list4)
    for i in range(count):
        for j in range(i + 1, count):
            if list4[i] >list4[j]:
                list4[i], list4[j] = list4[j], list4[i]
    str1=''
    for i in range(len(list4)):
        str1=str1+list4[i]
    str1=str1.strip()
    eng.append(str1)
for s in range(len(eng)-1):
    for j in range(s+1,len(eng)):
        if eng[s]==eng[j]:
            eng[j]=0
ans=0
for i in range(len(eng)):
    if eng[i]!=0:
        ans=ans+1
print(ans,end='')