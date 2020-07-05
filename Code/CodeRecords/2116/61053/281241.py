def insert(n:int,lst:list,beg:int):
    index = beg
    while index < len(lst):
        if lst[index] < n:
            index += 1
        elif lst[index] == n:
            return
        else:
            break
    if index == len(lst):
        lst.append(n)
    else:
        lst.insert(index,n)

def ugly(n,factor:list):
    lst = [1]
    beg = 0
    while len(lst)<n or lst[beg]*factor[0] < lst[n-1]:
        for no in factor:
            insert(lst[beg] * no, lst, beg)
        beg += 1
    return lst[n-1]

if __name__ == "__main__":
    n = int(input())
    factor = list(map(int,input().split(',')))
    print(ugly(n,factor))