def divide(y):
    return y//2


def plus(y):
    return y+1


if __name__=="__main__":
    x=int(input())
    y=int(input())
    cnt=0
    while y>x:
        if y%2!=0:
            y+=1
        else:
            y=y//2
        cnt+=1
    print(cnt+x-y)