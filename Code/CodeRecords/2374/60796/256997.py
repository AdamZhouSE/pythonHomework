n = int(input())
result=[]
while n > 0:
    string=""
    length = int(input())
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    # 先把数组里的元素从小到大排序
    length = length - 1
    while length > 0:
        i = 0
        for j in range(length):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
            i = i + 1
        length = length - 1
    # 再根据频率排序:
    count=[]
    for i in range(len(ls)):
        count.append(ls.count(ls[i]))
    while len(count)>0:
        m=max(count)#现在的最高频率
        i=count.index(m)
        a=ls[i]#最高频率的排前面的那个元素
        j=0
        while j<len(ls):
            if ls[j]==a:
                string=string+str(a)+" "
                del ls[j]
                del count[j]
                j=j-1
            j=j+1
    #每行的最后面有个空格
    result.append(string)
    n=n-1

for i in range(len(result)):
    print(result[i])












