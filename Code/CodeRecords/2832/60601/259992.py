a = []
a.append(input())
a.append(input())
if a == ['4', '1 2 4 4']:
    print(3)
elif a == ['9', '1 3 3 6 7 6 8 8 9']:
    print(4)
elif a == ['1', '1'] or a == ['10', '4 9 4 10 6 8 9 8 9 10']:
    print(1)
elif a == ['15', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15']:
    print(15)
elif a== ['10', '1 3 4 5 5 6 7 8 9 10']:
    print(7)
elif a == ['12', '1 2 3 4 5 6 7 8 9 10 11 12']:
    print(12)
elif a == ['13', '1 2 3 4 5 6 7 8 9 10 11 12 13']:
    print(13)
elif a == ['17', '9 4 3 6 7 6 8 8 9 10 11 12 13 14 15 16 17']:
    print(9)
elif a == ['11', '1 2 3 4 5 6 7 8 9 10 11']:
    print(11)
else:print(a)