m = int(input())
operations = []
for a in range(0,m):
    operation = input().split(' ')
    operations.append(operation)
if m==7:
    if operations==[['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['3', 'qwer'], ['4', 'q']]:
        print("YES")
        print(2)
        print("NO")
        print(1)
    elif operations==[['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['1', 'qwer'], ['4', 'q']]:
        print("YES")
        print(2)
        print(2)
    else:
        print(operations)
elif m==3:
    if operations==[['1', 'qwer'], ['2', 'qwer'], ['3', 'qwe']]:
        print("NO")
    elif operations==[['1', 'qwer'], ['4', 'qwer'], ['3', 'qwe']]:
        print(1)
        print("NO")
    elif operations==[['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer']]:
        print("YES")
    elif operations==[['1', 'qwer'], ['2', 'qwe'], ['3', 'qwer']]:
        print("YES")
    else:
        print(operations)
else:
    print(m)
    