def main():
    list0 = list(map(int, input().split(",")))
    target = int(input())
    if finds(list0,target)!=-1:print(True)
    else:
        print(False)
def finds(list0,target):
    num = -1
    for i in range(len(list0)):
        if list0[i]==target:
            num = i
            break
    return num
if __name__ == '__main__':
    main()