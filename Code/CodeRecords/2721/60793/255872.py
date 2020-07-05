ls = []
for i in range(0, int(input())):
    ls.append(list(map(int, input().split(" "))))
for sub_ls in ls:
    print(int(str(bin(sub_ls[0]))[2:]) * int(str(bin(sub_ls[1]))[2:]))