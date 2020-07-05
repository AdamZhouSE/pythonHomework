num = int(input())
string = input()
ones = 0
for i in string:
    if i == "1":
        ones = ones + 1
res = "1"
for i in range(num-ones):
    res = res + "0"
print(res,end="")