num=int(input())
list=[]
for i in range(0,num):
    temp=input().split(" ")
    if not temp in list:
        list.append(temp)
print(len(list))