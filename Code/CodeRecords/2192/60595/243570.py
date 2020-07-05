def Test():
    num=int(input())
    save=num
    line=[]
    line.append(num)
    print(num,end=" ")
    num=num-5
    check=False
    while(num!=save):
        print(num,end=" ")
        if(num<=0):
            check=True
        if(check):
            num=num+5
        else:
            num=num-5
    print(num, end=" \n")

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()