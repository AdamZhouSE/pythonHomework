from math import ceil


def find(lst,n,tar):
    low = 0
    high = n-1
    mid = ceil((high+low)/2)
    while low < high:
        if high - low == 1:
            if abs(lst[low]-tar) < abs(lst[high]-tar):
                return lst[low]
            else:
                return lst[high]
        mid = ceil((low + high) / 2)
        if lst[mid] == tar:
            return lst[mid]
        if lst[mid] < tar:
            low = mid
        else:
            high = mid
    return lst[mid]

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        n,tar = map(int,input().split())
        lst = list(map(int,input().split()))
        ans.append(find(lst,n,tar))
    for res in ans:
        print(res)