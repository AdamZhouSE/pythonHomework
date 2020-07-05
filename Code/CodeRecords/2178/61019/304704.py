read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
ns = read_line()
sync = set()
magic = []
for n in ns:
    magic.append(n)
    for i in range(len(magic)):
        r = magic[i:]
        # print(r)
        sync.add(''.join([str(n) for n in r]))
    print(len(sync))
