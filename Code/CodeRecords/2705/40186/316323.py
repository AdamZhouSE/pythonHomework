a = eval(input())
b = []
for i in a:
    if int(i[0]) in b and int(i[1]) in b:
        print(i)
    else:
        for j in i:
            if not(int(j) in b):
                b.append(int(j))