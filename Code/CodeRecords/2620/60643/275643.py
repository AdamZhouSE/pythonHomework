if __name__=="__main__":
    test=int(input())
    for i in range(test):
        n=eval(input())
        sum=0
        for i in range(n+1):
            sum+=i**5
        print(sum)