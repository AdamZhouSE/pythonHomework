cnt = int(input())
li = []
for i in range(cnt):
    li.append(str(input()))
for string in li:
    cntStr = len(string)
    cntSet = len(set(string))
    if cntSet == cntStr:
        print("1")
    else:
        print("0")