def swap(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def sort(lst,n):
    p0 = 0
    p2 = n - 1
    while p0 < n and lst[p0] == 0:
        p0 = p0 + 1
    while p2 > -1 and lst[p2] == 2:
        p2 = p2 - 1
    swap(lst,p0,p2)
    p1 = p0 + 1
    while p1 <= p2:
        if lst[p1] == 1:
            p1 = p1 + 1
        elif lst[p1] == 0:
            swap(lst,p1,p0)
            while p0 < n and lst[p0] == 0:
                p0 = p0 + 1
        else:
            swap(lst,p1,p2)
            while p2 > -1 and lst[p2] == 2:
                p2 = p2 - 1

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        sort(numlst,n)
        ans.append(numlst)
    for res in ans:
        print(*res)