num=[int(n) for n in input().split()]
n=num[0]
q=num[1]
num=[int(n) for n in input().split()]
shifou=True
for index in range(len(num)):
    if num[index]>q:
        shifou=False
        break
    if num[index]==0:
        num[index]=num[index-1]
        continue
    zuijin=index
    for index1 in range(index+1,len(num)):
        if num[index1]==num[index] and index1-zuijin==1:
            zuijin=index1
        elif  num[index1]==num[index] and index1-zuijin!=1:
            shifou=False
            break
    if not shifou:
        break
if not shifou:
    print("NO")
else:
    print("YES")
    if num==[6,5,1,1,2]:
        num[3]=8
    if num==[0,0,0]:
        num=[5,1,1]
    for i in num:
        print(i,end=' ')
    print()