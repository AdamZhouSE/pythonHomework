length=int(input())
string=input()
hzlist=[]
for i in range(length):
    hzlist.append(string[i:])

str0=input()
list0=str0.split()
listnum=[]
for x in list0:
    listnum.append(int(x))

maxnum=0
for i in range(length):
    for j in range(i+1,length):
        first=hzlist[i]
        second=hzlist[j]
        temp=0
        for i in range(len(second)):
            if(first[i]==second[i]):
                temp+=1
            else:
                break
        temp=temp+listnum[i]+listnum[j]
        
        if(temp>maxnum):
            maxnum=temp
print(maxnum)