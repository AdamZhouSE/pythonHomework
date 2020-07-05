if __name__ == '__main__':
    temp = input().split(",")
    n = int(input())
    list=[]
    for item in temp:
        list.append(int(item))
    list = []
    k=0
    for item in list:
        a=n-item
        if a in list and a!=item:
            result=[list.index(item),list.index(a)]
            print(result)
            break