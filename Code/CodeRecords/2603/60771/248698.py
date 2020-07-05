#34
ori = input() #此处接收到的是一个列表样的string，不要上当
oriList = list(ori)
num = [int(item) for item in ori if item<='9' and item>='0']
k = int(input())
n = len(num)
length = [] #存放长度绝对值
for i in range(0,n-1):
    for j in range(i,n):
        l = abs(num[i]-num[j])
        length.append(l)
length.sort()
print(length[k-1])
