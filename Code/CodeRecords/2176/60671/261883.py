str0=input()
length=len(str0)
list0=[]
list1=[]
for i in range(length):
    list0.append(str0[i:])
    list1.append(str0[i:])

list1.sort()
num=[]
for m in list1:
    num.append(list0.index(m)+1)
    
print(*num)

    