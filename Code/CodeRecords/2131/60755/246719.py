def ap(num):
    flag = True
    for i in range(len(num) - 1):
        if int(num[i+1]) - int(num[i]) != int(num[1]) - int(num[0]):
            flag = False
            break
    return flag


num = input().split(",")
sum = 0
for i in range(3, len(num)+1):
    for k in range(len(num) - i + 1):
        if ap(num[k:k+i]):
            sum = sum + 1
print(sum)