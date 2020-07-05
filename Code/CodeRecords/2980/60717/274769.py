list1=list(input())
n=input().split()
wrong=0
if n[0]=='D':
    try:
        list1.remove(n[1])
    except:
        wrong=1
if n[0]=='I':
    for i in range(0,len(list1)):
        if list1[len(list1)-1-i]==n[1]:
            list1.insert(len(list1)-1-i, n[2])
            break
if n[0]=='R':
    flag=0
    for i in range(0,len(list1)):
        if list1[i]==n[1]:
            list1[i]=n[2]
            flag=1
    if flag==0:
        print('no exist')
output=''
for i in list1:
    output+=i
print(output)