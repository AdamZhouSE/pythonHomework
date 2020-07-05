s=input()

m=int(input())

numlist=[]
sl=list(s)
for i in sl:
    numlist.append(ord(i)-65+m)
num=''
for i in numlist:
    num=num+str(i)
temp=list(num)

while int(num)>100:
    t=[]
    for i in range(len(temp)-1):
        x=int(temp[i])+int(temp[i+1])
        if(x>=10):
            x=x-10
        t.append(x)

    temp.clear()
    temp=t
    num=''
    for i in temp:
        num=num+str(i)

print(int(num),end='')