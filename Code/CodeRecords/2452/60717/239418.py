n = int(input())
list1=[]
for i in range(0,n):
    list2=input().split(',')
    for j in range(0,len(list2)):
        list1.append(int(list2[j]))
        
target=int(input())

if target in list1:
    print(True)
else:
    print(False)
    