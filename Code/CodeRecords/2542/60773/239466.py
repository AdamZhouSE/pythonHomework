start=input()
s=start[1:len(start)-1]
list=s.split(',')
num = len(list)
for i in range(num):
    list[i]=int(list[i])
list.sort()
max=1
sum=1
for i in range(num-1):
    if int(list[i+1])==int(list[i])+1:
        sum=sum+1
    else:
        if sum>max:
            max=sum
        sum=1
print(max)