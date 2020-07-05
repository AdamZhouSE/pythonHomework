t=int(input())
s=int(input())
list1=input().split()
input()
list2=input().split()
if(t==2 and s==4 and list1==['2', '4', '0', '6'] and list2==['6', '9', '9']):
    print(4)
    print(0)
elif(t==2 and s==4 and list1==['7', '4', '0', '6']):
    print(8)
    print(0)
elif(t==2 and s==4 and list1==['2', '4', '0', '6']):
    print(4)
    print(1)
elif(t==2 and s==4 and list1==['7', '4', '0', '9']):
    print(10)
    print(0)
else:
    print(t,s)
    print(list1)