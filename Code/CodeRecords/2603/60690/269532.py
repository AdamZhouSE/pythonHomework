list=input()
list=list[1:-1]
list=list.split(",")
k=int(input())

value=[]
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        value.append(abs(int(list[i])-int(list[j])))
value.sort()
print(value[k-1])