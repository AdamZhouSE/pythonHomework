if __name__ == "__main__":
    n=int(input())
    coins=list(map(int,input().split()))
    st=set(coins)
    counter=[]
    for i in st:
        counter.append(coins.count(i))
    print(max(counter))