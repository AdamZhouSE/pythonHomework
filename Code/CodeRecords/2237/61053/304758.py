def f(lst,a,b):
    temp = lst[a:b+1]
    temp = temp[::-1]
    for i in range(a,b+1):
        lst[i] = temp[i-a]

if __name__ == "__main__":
    n,m = map(int,input().split(" "))
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    for i in range(m):
        a, b = map(int,input().split(" "))
        f(lst,a-1,b-1)
    for k in range(n):
        print(lst[k],end=" ")