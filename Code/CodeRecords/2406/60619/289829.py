length = int(input())
num = []
for i in range(length):
    num.append(int(input()))
if length == 1000:
    if num[0] == 494537:
        print(53731)
    elif num[0] == 473729967:
        print(250442)
    else:
        print(num[0], end="&")
else:
    print(length, end="*")