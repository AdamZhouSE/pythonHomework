def h1():
    n = int(input())
    arr = []
    for i in range(n):
        temp = list(input())
        temp.sort()
        s = str(temp)
        # s = ""
        # for j in range(len(temp)):
        #     s += temp[j]
        arr.append(s)
    kind = 0
    for i in range(n):
        kind += 1
        for j in range(i):
            if(arr[j]==arr[i]):
                kind -= 1
                break;
    print(kind,end="")

if __name__ == '__main__':
    h1()