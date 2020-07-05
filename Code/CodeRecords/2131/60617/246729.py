def main():
    arr=input()
    arr=list(map(int, arr.split(",")))
    numOfAp=0
    N=len(arr)
    Aplen=2
    Apcount=0
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]==arr[i-1]-arr[i-2]:
            Apcount=Apcount+Aplen-1
            Aplen+=1
        else:
            Aplen=2
    print(Apcount)

if __name__=='__main__':
    main()
