def code(string, twice):
    for index in range(len(string)):
        if '0' <= string[index] <= '9':
            twice = int(string[index])
        elif string[index] == '[':
            code(string[index + 1:], twice)
        elif 'a' <= string[index] <= 'z':
            result = ''
            for k in range(twice):
                result = result + string[index] + code(string[index + 1:], 1)
            return result
        elif string[index] == ']':
            return ''


num = int(input())
for i in range(num):
    Str = input()
    res = code(Str, 0)
    print(res)
