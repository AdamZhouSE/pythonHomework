def main():
    arr=list(map(int, input().split(",")))
    count=0
    Min=min(arr)
    for i in arr:
        count+=i-Min
    print(count)

if __name__=='__main__':
    main()