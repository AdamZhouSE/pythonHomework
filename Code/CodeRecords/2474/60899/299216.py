numOftests = int(input())
for i in range(numOftests):
    s = input()
    sum0 = 0
    list0 = []
    for j in range(len(s)):
        if s[j]=="(":
            list0.append("(")
        else:
            if list0 == []:
                continue
            else:
                sum0+=2
                list0.remove("(")
    print(sum0)