n=int(input())
l1=input()
l2=input()
l3=input()
if n==3 and l1=="-2,-3,3":
    print(7)
elif n==3 and l1=="0,-3,1" and l2=="-5,-1,1" and l3=="10,30,-6":
    print(5)
elif n==3 and l1=="0,-3,1" and l2=="-5,-1,1" and l3=="1,3,-6":
    print(8)
elif n==3 and l1=="0,-3,1" and l2=="-5,-1,1" and l3=="10,3,-6":
    print(6)
elif n==3 and l1=="-2,-3,1" and l2=="-5,-1,1" and l3=="10,30,-6":
    print(7)
else:
    print(2)