def test3():
    n=int(input())
    person=input().split(" ")
    num=set(person)
    l=len(num)
    for item in num:
        if item == "0":
            l-1
    return l
print(test3())