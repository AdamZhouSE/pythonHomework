s = []
newlst = []
num = int(input())
for i in range(num):
    temp = input()
    lst = list(temp)
    length = len(lst)
    for j in range(length):
        if j != length - 1:
            if lst[j] != lst[j+1]:
                newlst.append(lst[j])
        else:
            if lst[-1] != lst[-2]:
                newlst.append(lst[-1])
    output = ''.join(newlst)
    print(output)
