def cal(n):
    if(n==1):
        return "A"
    else:
        return cal(n-1)+('A'+n-1)+cal(n-1)
if __name__=='__main__':
    n = int(input())
    print(cal(n))
    print('\n')

