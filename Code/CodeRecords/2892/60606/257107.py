line = input().split(" ")
n = int(line[0])
m = int(line[1])
string = ""
if n == 0:
    n += 1
for i in range(n,m+1):
    string += str(i)
for i in range(9):
    print(string.count(str(i)),end=" ")
print(string.count(str(9)),end="")