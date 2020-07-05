def h15():
    s = input().split()
    n1,n2 = map(int,s)
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = []
    for i in range(n2):
        temp = 0
        for j in range(n1):
            if(arr1[j]<=arr2[i]):
                temp += 1
        res.append(temp)
    for i in range(n2-1):
        print(res[i],end=" ")
    print(res[n2-1])

if __name__ == '__main__':
    h15()