n=int(input())
list1=[]
for i in range(0,n):
    list1.append(input().split(','))
    
list2=input().split(',')

minn=999
for i in range(0,n):
    minn=min(int(list1[i][0])-int(list2[0])+int(list1[i][1])-int(list2[1]),minn)
    
if int(list2[0])+int(list2[1])<minn or ((int(list2[0])+int(list2[1]))-minn)%2==1:
    print(True)
else:
    print(False)