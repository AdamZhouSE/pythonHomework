num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
slj=0
dm=0

for i in range(num):
    index=0
    if list[0]>list[-1]: index=0
    else: index=-1

    if i%2==0: slj+=list[index]
    else: dm+=list[index]

    list.pop(index)

print(str(slj)+" "+str(dm))