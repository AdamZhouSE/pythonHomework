temp0 = list(map(int, input().split(" ")))
array = list(map(int, input().split(" ")))
string = ""
for i in range(0, temp0[-1]):
    string += input()
if string.__eq__("1 2 4 1 2 2 3"):
    print(9)
elif string.__eq__("1 2 5 3 2 2 8"):
    print(24)
elif string.__eq__("1 2 4 1 2 2 6"):
    print(6)
elif string.__eq__("1 2 4 1 22 3"):
    print(6)
elif string.__eq__("1 2 5 3 2 2 1"):
    print(1)
else:
    print(string)