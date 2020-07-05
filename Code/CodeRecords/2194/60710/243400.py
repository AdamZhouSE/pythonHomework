#生成两个数字之间所有的素数
def judge(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
def solve(S):
    S1=S.split(" ")
    low1=int(S1[0])
    high1=int(S1[1])
    this_num=[]
    for i in range(low1,high1+1):
        if judge(i):
            this_num.append(i)
    return this_num

if __name__ == '__main__':
    m1=int(input())
    count=0
    while count<m1:
        the_num=input()
        result=solve(the_num)
        re = [str(j) for j in result]
        for k in range(0, len(re)):
            if k==len(re)-1:
                print(re[k], end='')
            else:
                print(re[k] + " ", end='')
        print("")
        count=count+1


