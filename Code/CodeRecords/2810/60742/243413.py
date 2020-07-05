n_str = input()
n = int(n_str)
res = []
while n>0:
    num = []
    for i in range(len(n_str)):
        if n_str[i]=='0':
            num.append('0')
        else:
            num.append('1')
    num_str = ''.join(num)
    n = n-int(num_str)
    res.append(num_str)
    n_str = str(n)
print(len(res))
print(' '.join(res))