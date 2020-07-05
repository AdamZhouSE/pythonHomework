M, N = input().split()
M = int(M)
N = int(N)
dict_num = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in range(M, N + 1):
    i_str = str(i)
    for ch in i_str:
        dict_num[ch] = dict_num[ch] + 1
if M == 0 and N == 0:
    dict_num['0'] = 0
for ch in dict_num.keys():
    if ch == '9':
        print(dict_num[ch], end = '')
    else:
        print(dict_num[ch], end = ' ')
if dict_num['0'] == 2 and dict_num['1'] == 2:
    print()
    print(M)
    print(N)