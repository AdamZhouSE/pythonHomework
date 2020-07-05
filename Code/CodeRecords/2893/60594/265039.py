num=eval(input())
for index in range(len(num)):
    zongshu=0
    for index1 in range(len(num)):
        if num[index]==num[index1]:
            zongshu+=1
    if zongshu==1:
        print(num[index])
        break