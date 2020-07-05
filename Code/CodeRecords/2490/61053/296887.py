def Intersect(lst1,lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    return list(s1&s2)

if __name__ == "__main__":
    lst1 = eval(input())
    lst2 = eval(input())
    res = Intersect(lst1,lst2)
    print(sorted(res))