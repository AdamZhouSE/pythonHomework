def perm(code, position, end):
    if position == end:
        perms.add(''.join(code))

    for index in range(position, end):
        code[position],code[index] = code[index], code[position]
        perm(code,position+1,end)
        code[position], code[index] = code[index], code[position]


string = input()
codes = []
perms = set()
n = int(input())
for i in range(n):
    codes.append(input())
count = 0
for code in codes:
    code = list(map(str,code))
    perm(code, 0, len(code))
for x in perms:
    if x in string:
        count += 1
print(count)