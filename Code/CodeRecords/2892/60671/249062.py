str1=input()
list1=str1.split()
start=int(list1[0])
end=int(list1[1])
count=[0]*10
for num in range(start,end+1):
    if(num!=0):
        for c in (str(num)):
            count[int(c)]+=1
print(*count,end='')