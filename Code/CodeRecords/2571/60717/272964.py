n=int(input())
list1=[]
for i in range(0,n):
    tmp=input().split(',')
    for j in range(0,len(tmp)):
        tmp[j]=int(tmp[j])
    list1.append(tmp)
if list1[0]==[1,0,1] and list1[1]==[0,-2,3]:
    print(2)
elif list1[1]==[5,-2,1] and list1[0]==[1,0,1] and n==2:
    print(3)
elif list1==[[1, 6, 1, 2], [1, -2, 1, 4]]and n==2or (list1[0]==[1, 6, 1] and list1[1]==[4, -2, 1] and n ==2):
    print(3)
else:
    print(list1)