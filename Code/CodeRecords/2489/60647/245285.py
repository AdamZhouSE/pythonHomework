list=input()
low=int(input())
high=int(input())
count=0
for i in range(len(list)):
    temp=0
    for j in range(i,len(list)):
        temp=temp+int(list[j])
        if temp>=low and temp<=high:
            count+=1
print(count)