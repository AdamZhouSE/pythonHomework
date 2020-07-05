n=int(input())
numlist=[]
for i in range(n):
    s=input()
    sl=s.split(',')
    temp=[]
    for x in sl:
        temp.append(int(x))
    numlist.append(temp)
m=int(input())
j=0
for i in numlist:
    if(m>=i[0] and m<=i[len(i)-1]):
        if(m in i):
            j=1
            break
if(j==1):
    print('True')
else:
    print('False')
