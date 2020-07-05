n=int(input())
list1=input().split()
j=0
d=0
turn='j'
for i in range(0,n):
    if(turn=='j'):
       if(int(list1[0])>int(list1[-1])):
           j=j+int(list1[0])
           del list1[0]
       else:
           j=j+int(list1[-1])
           del list1[-1]
       turn='d'
    else:
       if(int(list1[0])>int(list1[-1])):
           d=d+int(list1[0])
           del list1[0]
       else:
           d=d+int(list1[-1])
           del list1[-1]
       turn='j'
print(j,d)
           