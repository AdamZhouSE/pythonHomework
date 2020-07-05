#判断一个数是否为完美数

def solve(num):
    re=[]
    for i in range(1,num):
        if num%i==0:
            re.append(i)
    return sum(re)==num
if __name__ == '__main__':
    a=int(input())
    print(solve(a))