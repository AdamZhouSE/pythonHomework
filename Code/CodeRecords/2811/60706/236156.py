full=input()
list1=full.split(' ')
p=int(list1[0])
n=int(list1[1])
list=[]
flag=0
for i in range(0,p):
    list.append('0')
for i in range(0,n):
    x=int(input())
    if list[x%p]=='0':
        list[x%p]='1'
    else:
        print(str(i+1))
        flag=1
        break
if(flag==0):
    print('-1')