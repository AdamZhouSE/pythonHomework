if __name__ == "__main__":
    lst = list(map(int,input().split(',')))
    k = int(input())
    if not k in lst:
        print("[-1, -1]")
    else:
        a = lst.index(k)
        i = a
        b = a
        while i < len(lst):
            if lst[i] == k:
                b = i
            i += 1
        print("[%d, %d]" %(a, b))
