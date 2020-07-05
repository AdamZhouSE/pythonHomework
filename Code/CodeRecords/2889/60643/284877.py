if __name__=="__main__":
    n=int(input())
    data=input().split()
    data=[int(x) for x in data]
    aver=sum(data)/n
    print("%.6f" % aver)