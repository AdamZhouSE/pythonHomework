str0 = input()
list0 = [[0 for i in range(2)]for j in range(len(str0))]
for i in range(len(str0)):
    list0[i][0] = str0[i]
    list0[i][1] = str0.count(str0[i])
list0.sort(key=lambda x:x[1],reverse=True)
for i in range(len(list0)):
    print(list0[i][0],end="")
print()