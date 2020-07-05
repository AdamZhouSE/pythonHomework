number=int(input())
allowed_errorscore=1e-5
list=[0]*number
i=0
for i in range(number):
    list1=input().split()
    list[i]=float((int(list1[0])+int(list1[1])+int(list1[2])+int(list1[3]))/4)
score=float(list[0])
list.sort(reverse=True)
for i in range (number):
    if abs(score - list[i]) <= allowed_errorscore:
        
        print(i+1)
        break