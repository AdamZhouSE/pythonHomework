n = int(input())
list1=[]
list2=[]

for i in range(0,n):
    list1=input().split()
    list2.append(list1)

for i in list2:
    print(int(i[1])**(int(i[0])-1))