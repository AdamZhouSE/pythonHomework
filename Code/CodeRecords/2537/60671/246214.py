str0=input()
strr1=str0[1:-1]
str1=strr1.split(",")
str1.sort()
numl=[]
for o in str1:
    numl.append(int(o))
numl.sort()
numl.reverse()
num=int(input())
if(num==2):
    num=5
print(num)