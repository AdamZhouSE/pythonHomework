if __name__ == "__main__":
    test=int(input())
    lst=[]
    for i in range(test):
        a=input().split()
        a=[int(x) for x in a]
        lst.append(a)
    for i in lst:
        sum=0
        k=i[1]
        n=i[0]
        sum=k**(n-1)
        print(sum)