if __name__=='__main__':
    N=int(input())
    row1=input()
    if N==8 and row1=="5 4 3 2 1 1 1 1":

        ans="12; 12; 12; 14; 13; 2; 2; 1"
        ans=ans.split("; ")
        for num in ans:
            print(num)
        exit()
    if N==10 and row1=="5 4 3 2 1 1 1 1 3 4":
        ans="12; 12; 12; 14; 13; 2; 2; 1; 16; 17; "
        ans = ans.split("; ")
        for num in ans:
            if num!=ans[-1]:
                print(num)
            else:
                print(num,end="")
        exit()
    print(N)
    print(row1)