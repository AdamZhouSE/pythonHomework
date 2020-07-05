n=int(input())
list1=0
num1=0
list2=0
num2=0
for i in range(n):
     str=input()
     temp=str.split( )
     if(int(temp[0])==1):
         list1=list1+int(temp[1])
         num1=num1+1
     else:
         list2=list2+int(temp[1])
         num2=num2+1
if list1>=num1*5:
    print("LIVE")
else:
    print("DEAD")
if list2>=num2*5:
    print("LIVE")
else:
    print("DEAD")