board = list(input().split(","))
result = True
o_count, x_count = 0, 0
flag_x = 0
flag_o = 0
for line in board:
    if line == "XXX":
        flag_x = 1
    elif line == "OOO":
        flag_o = 1
if flag_x == 1 and flag_o == 1:
    result = False
print(result)