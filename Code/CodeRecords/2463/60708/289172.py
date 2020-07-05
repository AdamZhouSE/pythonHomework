if __name__ == '__main__':
    temp = input().split(",")
    list = []
    k=0
    n=int(input())
    for item in temp:
        a=n-item
        if a in temp and a!=item:
            print(temp.index(a))
            break