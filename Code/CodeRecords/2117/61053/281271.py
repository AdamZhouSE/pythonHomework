def cal(n):
    lst = []
    for i in range(n):
        lst.append(0)
    for i in range(n):
        for j in range(i,n,i+1):
            lst[j] = lst[j]^1
    count = 0
    for i in lst:
        if i == 1:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(cal(n))