
if __name__ == "__main__":
    testNO = int(input())
    for i in range(0,testNO):
        n,m = map(int,input().split())
        lst1 = list(map(int,input().split()))
        lst2 = list(map(int,input().split()))
        lst1 = sorted(lst1)
        lst2 = sorted(lst2)
        index1 = 0
        index2 = 0
        lst = []
        while index1 < n and index2 < m:
            if lst1[index1] < lst2[index2]:
                lst.append(lst1[index1])
                index1 += 1
            else:
                lst.append(lst2[index2])
                index2 += 1
        if index1 == n:
            for i in range(index2,m):
                lst.append(lst2[i])
        else:
            for i in range(index1,n):
                lst.append(lst1[i])
        for no in lst:
            print(no,end=" ")
        print()