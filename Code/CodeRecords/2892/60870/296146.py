M, N = input().split()
M = int(M)
N = int(N)
dict_num = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in range(M, N + 1):
    i_str = str(i)
    for ch in i_str:
        dict_num[ch] = dict_num[ch] + 1
for i in dict_num.values():
    print(i, end = ' ')