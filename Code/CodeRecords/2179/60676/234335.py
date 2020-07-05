def common_prefix(str1, str2):
    i = 0
    while i<len(str1) and i<len(str2):
        if str1[i]==str2[i]:
            i += 1
        else:
            break
    return i

count = int(input().split()[1])
string = input()
res = []
for i in range(count):
    myList = input().split()
    res.append(common_prefix(string[int(myList[0])-1: int(myList[1])], string[int(myList[2])-1: int(myList[3])]))
for i in range(len(res)):
    print(res[i])