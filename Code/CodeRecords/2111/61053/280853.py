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

def ugly(n):
    lst = [1]
    beg = 0
    while len(lst)<n or lst[beg]*2 < lst[n-1]:
        insert(lst[beg] * 2, lst, beg)
        insert(lst[beg] * 3, lst, beg)
        insert(lst[beg] * 5, lst, beg)
        beg += 1
    return lst[n-1]

if __name__ == "__main__":
    n = int(input())
    print(ugly(n))