num = int(input())
string = bin(num)[2:]
count = 0
for s in string:
    if s == "1":
        count += 1
        if count == 2:
            break
if count == 1:
    print(True)
else:
    print(False)
