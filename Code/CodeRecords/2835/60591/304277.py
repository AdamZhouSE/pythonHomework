input()
temp = list(map(int,input().split(" ")))
te = {}
te[0] = 0
te[5] = 0
for m in temp:
    te[m] += 1
number = (int) (te[5] / 9)
result = ""
for x in range(number*9):
    result += "5"
if(number == 0):
    if(te[0] == 0):
        print(-1)
    else:
        print("0")
else:
    if(te[0] == 0):
        print(-1)
    else:
        for x in range(te[0]):
            result += "0"
        print(result)