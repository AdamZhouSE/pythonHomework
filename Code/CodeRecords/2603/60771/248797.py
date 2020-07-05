#34
#处理原始输入的时候，要考虑两位数的情况..
ori = input() #此处接收到的是一个列表样的string，不要上当
oriList = list(ori) #转成list是因为其支持操作更多
num = []
for i in range(0,len(oriList)):
    if oriList[i]<='9' and oriList[i] >='0':
        str_ = oriList[i]
        j = i + 1
        while oriList[j]<='9'and oriList[j]>='0':
            str_ += oriList[j]
            oriList[j] = "-"
            j += 1
        num.append(int(str_))
k = int(input())
n = len(num)
length = [] #存放长度绝对值
for i in range(0,n-1):
    for j in range(i+1,n):
        l = abs(num[i]-num[j])
        # print(str(num[i])+" - "+str(num[j])+" = "+str(l))
        length.append(l)
length.sort()
print(length[k-1])