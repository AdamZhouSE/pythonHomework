#判断一个数是不是回文数
def solve(num):
    s=str(num)
    for i in range(0,len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
if __name__ == '__main__':
    a=int(input())
    print(solve(a))