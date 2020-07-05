def judge(num):
    if num==0:
        return False
    s=str(num)
    for k in s:
        if int(k)==0:
            return False
        if num%(int(k))!=0:
            return False
    return True
def solve(low,high):
    re=[]
    for i in range(low,high+1):
        if judge(i):
            re.append(i)
    return re
if __name__ == '__main__':
    l=int(input())
    h=int(input())
    print(solve(l,h))