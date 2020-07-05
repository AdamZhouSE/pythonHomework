def cal(n):
    if(n==1):
        print("A",end="")
    else:
        cal(n-1)
        print('A'+n-1,end="")
        cal(n-1)
if __name__=='__main__':
    n = int(input())
    cal(n)
    print("\n")
    


