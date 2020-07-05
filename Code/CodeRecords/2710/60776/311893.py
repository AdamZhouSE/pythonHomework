list=[]
a=input().split(' ')
renshu=int(a[0])
yujushu=int(a[1])
for i in range(0,yujushu):
    a=input().split(' ')
    if a[0]=='M':
        list1=[]
        list1.append(int(a[1]))
        list1.append(int(a[2]))
        list.append(list1)
    else:
        list1=[]
        for j in range(0,len(list)):
            if list[j][0]<=int(a[1]) and list[j][1]>=int(a[2]):
                list1.append(list[j][1])
        list1.sort()
        if list1==[]:
            print(-1)
        else:
            print(list1[0])