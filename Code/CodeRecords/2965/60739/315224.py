def CutAndInsert(str, a, b, c, m):
    cut = str[a:b]
    out_str = str[:c] + cut + str[c:len(str)]
    if len(out_str) > m:
        out_str = out_str[:m]
    return out_str

def process(str, command_list, k, m):
    for i in command_list:
        str = CutAndInsert(str, i[0], i[1], i[2], m)
    out_str = str[:k]
    return out_str

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input_str = getInput()
k = input_str[0]
m = input_str[1]

str = str(input())

n = int(input())
command_list = []
for i in range(n):
    command_list.append(getInput())

print(process(str, command_list, k, m), end='')