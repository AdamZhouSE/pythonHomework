pre = list(input())
s = []
for ele in pre:
    if ele != '#':
        s.append(ele)
    else:
        if len(s) != 0:
            print(s.pop(),end=" ")
            #s.pop()

