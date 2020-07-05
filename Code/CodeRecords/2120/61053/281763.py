def f(n):
    lst = [0,1,1]
    for i in range(3,n+1):
        lst.append(i-1)
        for j in range(1,int(i/2)+1):
            lst[i] = max(max( max(j*(i-j),lst[j]*lst[i-j]) , max(j*lst[i-j],lst[j]*(i-j))),lst[i])
    return lst[n]

if __name__ == "__main__":
    n = int(input())
    print(f(n))