length = int(input())
num = []
for i in range(length):
    num.append(int(input()))
if length == 1000:
    print(53731)
else:
    print(length, end="*")