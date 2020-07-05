#N的序列问题

def solve(num):
    re=[]
    num2=num
    while num2>0:
        re.append(num2)
        num2 = num2 - 5
    num1=num2

    while num1<num:
        re.append(num1)
        num1=num1+5
    re.append(num)
    return re

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        result=solve(num)
        re = [str(j) for j in result]
        for k in range(0, len(re)):
            print(re[k] + " ", end='')
        print("")
        c=c+1