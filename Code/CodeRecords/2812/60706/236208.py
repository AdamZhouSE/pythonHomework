n=input()
m=input()
list=m.split(' ')
list.sort()
ans=int(0)
for i in range(0,len(list)-1):
    if(list[i]==list[i+1]):
        list[i]='0'
for i in list:
    if i!='0': 
        ans=ans+1
print(ans)