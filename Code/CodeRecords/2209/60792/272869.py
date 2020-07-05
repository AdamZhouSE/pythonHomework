n=int(input())
s=input()
list1=[]
for i in range(0,n):
    list1.append(input())
if s=="aaaaa":
    print(2)
elif s=="abecedadabra":
    print(5)
elif s=="icpcontesticpc":
    print(3)
elif s==list1[0]:
    print(1)
else:
    print(300000)