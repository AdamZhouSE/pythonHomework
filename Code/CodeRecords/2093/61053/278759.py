def factor(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res

def perm(n,k):
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    ans = ""
    while len(lst) > 0:
        n = len(lst) - 1
        fact = factor(n)
        index = int((k - 1) / fact)
        k = k % fact
        ans = ans + str(lst[index])
        #print(ans)
        del lst[index]
    print(ans)

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    perm(n,k)