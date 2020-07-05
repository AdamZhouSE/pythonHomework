def main():
    condition=input()
    condition=condition.split("; k = ")
    arrNum=list(map(int, condition[0].split(",")))
    k=int(condition[1])
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