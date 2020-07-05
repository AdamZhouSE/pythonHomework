string = input()
s = input()
m = ''
for i in range(len(s)):
    if s[i] != ' ':
        m += s[i]
if m[0] == 'D':
    for i in range(len(string)):
        if string[i] == m[1]:
            list_string = list(string)
            list_string.pop(i)
            string = ''.join(list_string)
            break
elif m[0] == 'I':
    if m[1] not in string:
        print("no exist")
    for i in range(len(string)-1, -1, -1):
        if string[i] == m[1]:
            string = string[0:i] + m[2] + string[i:len(string)]
            break
elif m[0] == 'R':
    if m[1] not in string:
        print("no exist")
    for x in string:
        string = string.replace(m[1], m[2])
print(string)
