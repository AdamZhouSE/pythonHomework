str=input()
length=len(str)
SA=[]

for i in range(0,length):
    SA.append(0)

i=length-1

while i>=0:
    rank=1
    temp=str[i:]
    for j in range(0,length):
        cmp=str[j:];
        Min=min(len(temp),len(cmp))
        for k in range(0,Min):
            if temp[k]==cmp[k]:
                if k==Min-1 and Min==len(cmp):
                    rank=rank+1
            elif temp[k]>cmp[k]:
                rank=rank+1
                break
            else:
                break
    SA[rank-2]=i+1
    i=i-1

for x in SA:
    print(x,end='')
    if x!=SA[length-1]:
        print(" ",end='')
print()