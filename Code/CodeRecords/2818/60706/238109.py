list=input()
list2=input()
list3=list.split(' ')
list4=list2.split(' ')
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
m=int(list3[1])
i=int(0)
ans=int(0)
if(list3[0]>list3[1]):
    while m>1:
        ans=ans+m*int(list4[i])
        i=i+1
        m=m-1
    for j in range(i,len(list4)):
        ans=ans+int(list4[j])
else:
    for i in range(0,len(list4)):
        ans=ans+m*int(list4[i])
        m=m-1
print(ans)
    