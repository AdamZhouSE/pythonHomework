
if __name__ == '__main__':
    n=int(input())
    a=n//3
    b=n%3
    if(b==0):
        max=pow(3,a)
    elif(b==2):
        max=pow(3,a)*2
    else:
        max=pow(3,a-1)*4
    if(n==2):
        max=1
    print(max)

