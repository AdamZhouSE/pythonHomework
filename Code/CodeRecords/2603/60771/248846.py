#34

ori = input()
oriList = ori[1:len(ori)-1]
oriList = oriList.split(",")
num = [int(item) for item in oriList]
k = int(input())
n = len(num)
length = [] #存放长度绝对值
for i in range(0,n-1):
    for j in range(i+1,n): #是i+1而不是i，不然就取到同一个值了
        l = abs(num[i]-num[j])
        # print(str(num[i])+" - "+str(num[j])+" = "+str(l))
        length.append(l)
length.sort()
print(length[k-1])