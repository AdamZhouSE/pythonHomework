def main():
    arrNum=list(map(int, input().split(",")))
    k=int(input())
    for i in range(0,len(arrNum)):
        temp=arrNum[i]
        for j in range(1,len(arrNum)):
            temp+=arrNum[j]
            if temp%k==0:
                print(True)
                exit()
    print(False)
if __name__=='__main__':
    main()