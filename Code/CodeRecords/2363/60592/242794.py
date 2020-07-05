num = int(input())
i = 1
index = 1
while index <= num:
    index = pow(2,i)
    i+=1
print(index-1-num)