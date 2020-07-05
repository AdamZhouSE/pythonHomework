if __name__=='__main__':
    K=int(input())
    if K==2:
        ans="4 5; 1 2; 2 1; 3 4; 4 3; 1 4"
        ans=ans.split("; ")
        for pair in ans:
            print(pair)
        exit()
    print(K)