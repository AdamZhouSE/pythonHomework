list1=eval(input())
lower=int(input())
higher=int(input())
count=0
for i in range(len(list1)):
    for j in range(i,len(list1)):
        base=0
        for k in range(i,j+1):
            base+=list1[k]
        if lower<=base<=higher:
            count+=1
print(count)