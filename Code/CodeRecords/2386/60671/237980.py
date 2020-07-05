time=int(input())
length=int(input())
str1=input()
list1=str1.split()
list2=[]
for c in list1:
    list2.append(int(c))
sum=0
for num in list2:
    sum+=num
have=False
target=int(input())
for x in range(length):
    