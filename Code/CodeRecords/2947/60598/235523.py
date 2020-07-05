times = int(input())
string = input()
for i in range(times):
    op = input().split(" ")
    if op[0] == "1":
        string += op[1]
        print(string)
    if op[0] == "2":
        start = int(op[1])
        length = int(op[2])
        string = string[start:start+length]
        print(string)
    if op[0] == "3":
        position = int(op[1])
        insert = op[2]
        string = string[0:position]+insert+string[position:]
        print(string)
    if op[0] == "4":
        print(string.find(op[1]))

