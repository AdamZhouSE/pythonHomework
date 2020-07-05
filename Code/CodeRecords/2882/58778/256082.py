n=int(input())
s=input()
sl=s.split( )
numlist=[]
for i in sl:
    numlist.append(int(i))
j=0
for i in range(len(numlist)-1):
    if(i==len(numlist)-2):
        print(numlist)
    if(numlist[i]==numlist[i+1]):
        break
    if(numlist[i]>numlist[i+1]):
        j=1
        break
index=i
if(1==len(numlist)):
    print("YES")
else:
    for i in range(index, len(numlist)):
        if (numlist[index] != numlist[i]):
            break
    endindex = i
    j = 0
    for i in range(endindex - 1, len(numlist) - 1):
        if (numlist[i] < numlist[i + 1]):
            j = 1
            break
    if (j == 1):
        print("NO")
    else:
        print("YES")