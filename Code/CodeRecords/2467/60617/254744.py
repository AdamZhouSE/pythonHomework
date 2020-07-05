def main():
    T=int(input())
    firstRow=input().split(" ")
    K=int(firstRow[2])
    M=list(map(int, input().split(" ")))
    N=list(map(int, input().split(" ")))
    M.extend(N)
    M.sort()
    print(M[K-1])

if __name__=='__main__':
    main()