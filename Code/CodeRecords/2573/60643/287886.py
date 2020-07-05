if __name__=="__main__":
    test=int(input())
    lst=[2,2,4,8,16,512,256,134217728,65536]
    for _ in range(test):
        n=int(input())
        print(lst[n-1])