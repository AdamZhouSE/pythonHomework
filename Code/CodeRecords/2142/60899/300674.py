numOftests = int(input())
for i in range(numOftests):
    s = input()
    list0 = []
    for x in s:
        if x=="(":
            list0.append("(")
            print(str(len(list0))+" ",end="")
        if x==")":
            list0.reverse()
            print(str(len(list0)-list0.index("("))+" ",end="")
            list0[list0.index("(")] = " "
            list0.reverse()
    print()