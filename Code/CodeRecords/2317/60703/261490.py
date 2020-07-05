listNum = [int(x) for x in input().split(",")]
all = 0
length = len(listNum)
for i in range(2**length):#不包含一个元素的情况
    temp = []
    for j in range(length):
        if(i >> j)%2 ==1:
            temp.append(listNum[j])
    temp.sort()
    if(len(temp)>1):
        all+= (temp[-1] - temp[0])

print(all%int(pow(10,9)+7))