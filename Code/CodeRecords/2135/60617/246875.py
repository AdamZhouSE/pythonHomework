def main():
    arr = list(map(int, input().split(",")))
    count=(max(arr)-min(arr))*len(arr-1)
    for i in arr:
        temple=0
        for j in arr:
            temple+=abs(j-i)
        if temple<count:
            count=temple
    print(count)

if __name__=='__main__':
    main()
    