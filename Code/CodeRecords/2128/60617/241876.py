def main():
    array=list(map(int, input().split(",")))
    MaxF=0
    n=len(array)
    for i in range(0,n):
        CurrentF=0
        for j in range(0,n):
            Idx=(j+i)%n
            CurrentF=CurrentF+j*array[Idx]
        if CurrentF>MaxF:
            MaxF=CurrentF
    print(MaxF)

if __name__=='__main__':
    main()