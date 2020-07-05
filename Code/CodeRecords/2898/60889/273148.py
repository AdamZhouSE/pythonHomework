input1 = input()
rawNum = input()
num = "1"
for i in rawNum:
    if i == "0":
        num = num + "0"
print(num,end = "")