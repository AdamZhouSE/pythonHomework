def nums_17_Alter(n):
    co = 0
    while n>1:
        if n==3:
            n-=1
        elif n%4==1:
            n-=1
        elif n%4==3:
            n+=1
        else:
            n/=2
        co+=1
    print(co)
if __name__=='__main__':
    n = int(input())
    nums_17_Alter(n)