from collections import defaultdict


fs = defaultdict(int)
do = input()
while do != '-1':
    if do.startswith('1'):
        w, c = map(int, do[2:].split(' '))
        if c not in fs.keys():
            fs[c] = w
    else:
        s_fs = sorted(fs)
        if do.startswith('3'):
            fs.pop(s_fs[0])
        else:
            fs.pop(s_fs[-1])
    do = input()
print(str(sum(fs.values())) + ' ' + str(sum(fs.keys())), end='')
