def cal(n):
    if(n==1):
        return "A"
    else:
        return str(cal(n-1))+chr(('A'+n-1))+str(cal(n-1))
if __name__=='__main__':
    n = int(input())
    string = cal(n)
    print(string,end='\n')


