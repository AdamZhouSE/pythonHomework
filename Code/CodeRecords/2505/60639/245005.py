num=input().strip('[').strip(']').split(',')
for i in range(len(num)):
    num[i]=int(num[i])
count=0
for i in range(len(num)):
    count=num.count(num[i])
    if count>=2:
        print(num[i])
        break
    else:
        continue