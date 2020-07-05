#大于等于N，且最接近2 的幂的数字

#判断这个数是不是2的幂
def judge(num):
    num = int(num)
    return True if num == 0 or num & (num - 1) == 0 else False

def solve(num):
    if judge(num):
        return num
    k=num
    while True:
        if judge(k):
            return k
        k=k+1

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        print(solve(num))
        c=c+1
