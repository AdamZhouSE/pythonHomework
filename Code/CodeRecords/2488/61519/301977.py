num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
num.sort(reverse=True)
mid = int(len(num) / 2)
num[1::2], num[0::2] = num[:mid], num[mid:]
for i in range(len(num)):
    num[i]=int(num[i])
print(num)