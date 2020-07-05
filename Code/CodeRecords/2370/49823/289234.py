def dq(n):
    if n==0:
        print(0)
        return
    res=''
    while n!=0:
        temp=n%(-2)
        if temp==0:
            res='0'+res
        else:
            res='1'+res
        n=(n+temp)/(-2)
    print(res)
if __name__ == '__main__':
    dq(int(input()))
