def pri(list,a):
    print(a[0],end="")
    left=a[1]
    right=a[2]
    leftloc=0
    rightloc=0
    for i in range(len(list)):
        if(list[i][0]==left):
            leftloc=i
        if(list[i][0]==right):
            rightloc=i
    if(left!='*'):
        pri(list, list[leftloc])
    if(right!="*"):
        pri(list, list[rightloc])






num=int(input())
list=[]
for i in range(num):
    string=input()
    list.append(string)
pri(list,list[0])
