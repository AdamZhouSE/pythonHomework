def cal(n):
    if(n==1):
        return "A"
    else:
        return cal(n-1)+chr(ord('A')+n-1)+cal(n-1)
if __name__=='__main__':
    n = int(input())
    string=cal(n)
    print(string,end="\n")
    


