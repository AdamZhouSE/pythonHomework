name=input()
name1=name.split('+')
list=[]
for  na in name1:
    if(na!='+'):
        list.append(na)
list.sort()
ans=''
for i in range(0,len(list)-1):
    ans=ans+list[i]+'+'
ans=ans+list[len(list)-1]
print(ans)
    