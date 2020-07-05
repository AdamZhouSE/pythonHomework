def getBinary(num):
    return '{:b}'.format(num)

num = int(input())
binStr = getBinary(num)
numOf1 = binStr.count("1")
if(numOf1<=1):
    print(0)
else:
    cnt = 1
    max = 0
    flag = False
    for i in range(0,len(binStr)):
        if(binStr[i]=="1"):
            if(not flag):
                flag = True
            if(cnt>max):
                max = cnt
            cnt = 1
        else:
            if(flag):
                cnt = cnt + 1
    print(max)
