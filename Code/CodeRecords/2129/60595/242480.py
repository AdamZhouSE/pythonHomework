def Test():
    num=int(input())
    count=0
    while(num!=1):
        if(num%2==0):
            num=num/2
        else:
            num=num-1
        count=count+1
    print(count)

if __name__ == "__main__":
    Test()