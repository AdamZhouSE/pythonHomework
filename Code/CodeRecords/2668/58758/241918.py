count = int(input())
ans = []
for i in range(0, count):
    old_num = int(input())
    num_str = bin(old_num)[2:]
    new_num = 2 ** (len(num_str)) - 1
    seq = []
    seq.append(new_num-old_num)
    seq.append(new_num)
    ans.append(seq)
for j in ans:
    print(j[0], j[1])
