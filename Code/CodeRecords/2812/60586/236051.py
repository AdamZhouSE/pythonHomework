def test3():
    n=int(input())
    person=input().split(" ")
    num=set(person)
    l=len(num)
    for item in num:
        if int(item) == 0:
            l-1
    if l==2:
        return 1
    return l
print(test3())