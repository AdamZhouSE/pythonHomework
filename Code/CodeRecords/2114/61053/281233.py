def minSum(n):
    lst = []
    lst.append(0)
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i - j**2 >= 0:
                if j == 1:
                    lst.append(lst[i-1]+1)
                else:
                    lst[i] = min(lst[i],lst[i-j**2]+1)
    return lst[n]

if __name__ == "__main__":
    n = int(input())
    print(minSum(n))