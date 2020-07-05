if __name__ == '__main__':
    temp = input().split(",")
    n = int(input())
    list=[]
    for item in temp:
        list.append(int(item))
    check=True
    k=0
    for item in list:
        a=n-item
        if a in list and a!=item:
            result=[list.index(item)+1,list.index(a)+1]
            print(result)
            check=False
            break
    if(check):
        print(None)
    