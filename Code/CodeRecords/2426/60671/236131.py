time=int(input())
num=int(input())
str=input()
list0=str.split()
list=[]
for x in list0:
    list.append(int(x))
list.sort()
list.reverse()

num=list[0]*list[1]*list[2]
print(num)