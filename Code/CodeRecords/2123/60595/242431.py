def Test():
    num=int(input())
    if(num==0):
        print(True)
    else:
        i=1
        sum=0
        check=False
        while(sum<=num):
            sum=sum+2*i-1
            i=i+1
            if(sum==num):
                check=True
        print(check)

if __name__ == "__main__":
    Test()