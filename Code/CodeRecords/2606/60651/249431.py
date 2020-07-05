mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
n=int(input())
l=len(list1)
s=0
for i in range(l):
    if list1[i]==n:
        print(i)
        s=1
        break
if s==0:
    print("-1")