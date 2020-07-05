
if __name__ == '__main__':
    n=int(input())
    a=n//3
    b=n%3
    if(b!=1):
        max=pow(3,a)
    else:
        max=pow(3,a-1)*4
    print(max)

