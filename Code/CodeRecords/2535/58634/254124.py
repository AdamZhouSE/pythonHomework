#左边块的最大数字 小于右边块的最小数
a = [int(i) for i in input().replace("[","").replace("]","").replace(","," ").split(" ")]
length = len(a)
result = 1
leftMax = a[0]
rightMin = [0]*length
rightMin[length-1] = a[length-1]
for i in range(length-2,-1,-1):
    rightMin[i] = min(a[i],rightMin[i+1])
#记录从当前位置开始到最后 最小的那个数字
#print(rightMin)
for i in range(1,length):
    if(rightMin[i]>=leftMax):
        result+=1
        leftMax = a[i]
    else:
        leftMax = max(a[i],leftMax)
print(result)