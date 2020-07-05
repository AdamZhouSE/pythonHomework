list=input().split(",")
num=int(input())
for i in range(len(list)):
    list[i]=int(list[i])
list.sort()
if(sum(list)==num):
    print(max(list))
else:
    print(int(num/len(list)+0.49))