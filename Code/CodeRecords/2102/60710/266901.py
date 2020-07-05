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
def solve(num):
    count=0
    for i in range(2,num):
        if judge(i):
            count=count+1
    return count
if __name__ == '__main__':
    a=int(input())
    print(solve(a))