def main():
    n=int(input())
    count=0
    if n==1:
        print(0)
        exit()
    else:
        while n!=1:
            if n%2==0:
                n=n/2
                count+=1
            else:
                n=n-1
                count+=1
    print(count)

if __name__=='__main__':
    main()