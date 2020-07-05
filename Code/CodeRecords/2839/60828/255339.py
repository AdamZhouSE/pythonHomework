def h11():
    n = int(input())
    arr = []
    res = []
    for i in range(n):
        s = input()
        res.append("NO")
        for j in range(len(arr)):
            if(s==arr[j]):
                res[len(res)-1] = "YES"
                break
        arr.append(s)
    for i in range(n):
        print(res[i])

if __name__ == '__main__':
    h11()