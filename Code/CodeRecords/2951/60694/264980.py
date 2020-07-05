a, b = input(), input()
N_2, N_3 = list(a), list(b)
dict = {"2": ["1", "0"], "1": ["2", "0"], "0": ["1", "2"]}

for i in range(len(N_2)):
    new2 = list(N_2)  # 注意复制列表要用list()
    new2[i] = "1" if new2[i] == "0" else "0"
    for j in range(len(N_3)):
        new3 = list(N_3)
        for k in range(2):
            new3[j] = dict[new3[j]][k]
            if int(''.join(new2), 2) == int(''.join(new3), 3):
                print(int(''.join(new2), 2), end="")
                exit()

