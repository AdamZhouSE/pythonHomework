def valid(string):
    output.add(string)
    if len(string) > 2:
        for i in range(1, len(string)-1):
            valid(string[:i]+string[i+1:])


vowel = ['a','e','u','i','o']
t = int(input())
for i in range(t):
    string = input()
    output = set()

    flags = []
    # flags = [1,0,0,1,0]
    for i in range(len(string)):
        if string[i] in vowel:
            flags.append(1)  # 元音为1
        else:
            flags.append(0)

    begin = end = -1
    while 1 in flags[begin+1:]:
        begin = flags.index(1, begin+1)
        end = begin
        while 0 in flags[end+1:]:
            end = flags.index(0, end+1)
            valid(string[begin:end+1])

    if len(output) == 0:
        print(-1)
    else:
        output = sorted(output)
        print(' '.join(output))