inp = input()
n_list = [int(inp[i]) for i in range(len(inp))]
sum = 0
pro = 1
for i in range(len(n_list)):
    sum += n_list[i]
    pro *= n_list[i]
print(pro - sum)