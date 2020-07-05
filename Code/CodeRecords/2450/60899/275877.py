
def main():
    list0 = list(map(int,input().split(",")))
    list1 = list(reversed(list0))
    target = int(input())
    print("[",end="")
    start = finds(list0,target)
    end = len(list0)-1-finds(list1,target)
    if finds(list0,target)==-1:print(-1,end="")
    else:print(start,end="")
    print(", ",end="")
    if finds(list1,target)==-1:print(-1,end="")
    else:print(end,end="")
    print("]")

def finds(list0,target):
    num = -1
    for i in range(len(list0)):
        if list0[i]==target:
            num = i
            break
    return num
if __name__ == '__main__':
    main()