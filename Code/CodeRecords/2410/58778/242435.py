s=input()
d=int(input())
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
count=[]
for i in range(len(numlist)):
    c=0
    temp=d
    for j in range(i,len(numlist)):
        if(numlist[j]-numlist[i]==temp):
            c=c+1
            temp=temp+d
    count.append(c)

print(max(count)+1)