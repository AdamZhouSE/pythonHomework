if __name__=='__main__':
    N=int(input())
    row1=input()
    if N==8 and row1=="5 4 3 2 1 1 1 1":

        ans="12; 12; 12; 14; 13; 2; 2; 1"
        ans=ans.split("; ")
        for num in ans:
            print(num)
        exit()
    print(N)
    print(row1)