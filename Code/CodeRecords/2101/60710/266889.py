def judge(num):
    if num==1:
        return True
    put=[] #用来存放出现过的平方和，如果平方和出现重复，那么这个数不是快乐数
    while num!=1:
        s=str(num)
        length=len(s)
        sum=0
        for i in range(0,length):
            sum=sum+(int(s[i])*int(s[i]))
        if sum==1:
            return True
        else:
            if put.count(sum)==0:
                put.append(sum)
            else:
                return False
        num=sum
if __name__ == '__main__':
    a=int(input())
    print(judge(a))