#40
#pro
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
a = 0 #三部分和初始化
b = 0
c = 0
count = 0
total = sum(num)
if total % 3 !=0:
    print(0)
else:
    avg = total//3
    for i in range(0,len(num)-2):
        a += num[i]
        if a == avg: #一旦满足就开始计算第二部分
            b = 0
            for j in range(i+1,len(num)-1):
                b += num[j]
                if b == avg:
                    c = 0
                    for k in range(j+1,len(num)):
                        c += num[k]
                    if c == avg:
                        count += 1
print(count)