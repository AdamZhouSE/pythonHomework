
#倒序一下，方便计算
#一辆车原本在他右边的车 现在在他左边 说明这辆车一定进行了超车
n = int(input())
array1 = [int(i) for i in input().split(" ")]
array1.reverse()
array2 = [int(i) for i in input().split(" ")]
array2.reverse()
result = 0
for i in range(n):
    for j in range(i+1,n):#他右边的车
        if(array2.index(array1[j])<array2.index(array1[i])):
            result += 1
            break

print(result)
