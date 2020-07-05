num=int(input())
list=[]
for i in range(0,num):
    arr=input().split(' ')
    list.append(arr)
asknum=int(input())
ask=[]
for i in range(0,asknum):
    arr=input()
    ask.append(arr)
re=[]
for i in range(0,asknum):
    key=ask[i]
    mark=0
    for j in range(0,num):
        if key in list[j]:
            print(j+1,end=" ")
            mark=1
    if mark==0:
        print(" ")
    else:
        print()
