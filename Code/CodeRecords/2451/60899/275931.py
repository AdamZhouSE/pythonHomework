def main():
    list0 = list(map(int, input().split(",")))
    target = int(input())
    if finds(list0,target)!=-1:print(finds(list0,target))
    else:
        tmp = len(list0)
        for i in range(len(list0)):
            if list0[i]>=target:
                tmp = i
                break
        print(tmp)
def finds(list0,target):
    num = -1
    for i in range(len(list0)):
        if list0[i]==target:
            num = i
            break
    return num
if __name__ == '__main__':
    main()