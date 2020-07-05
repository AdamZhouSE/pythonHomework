string = input()
s = input()
x = s[3]
if s[0] == 'D':
    for i in range(len(string)):
        if string[i] == s[3]:
            list_string = list(string)
            list_string.pop(i)
            string = ''.join(list_string)
            break
elif s[0] == 'I':
    for i in range(len(string)-1, -1, -1):
        if string[i] == s[3]:
            string = string[0:i] + s[5] + string[i:len(string)]
            break
elif s[0] == 'R':
    for x in string:
        string = string.replace(s[3], s[5])
print(string)
