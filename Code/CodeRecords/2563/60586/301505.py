def exam8():
    s=input()
    n=int(s[1:len(s)-1])
    print(999999999999999999,end="")
    if n==1:
        print(1)
        return 
    for i in range(2,n):
        sum=1
        j=1;
        while True:
            sum+=i**j
            j+=1
            if sum==n:
                print(i)
                return 
            if sum>n:
                break
exam8()                