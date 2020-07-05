def calculation(s):
    start = []
    end = []

    if not '[' in s:
        print(s, end='')
    else:
        for i in range(len(s)):
            if s[i] == '[':
                start.append(i)
            elif s[i] == ']':
                end.append(i)

        for j in range(start[0]):
            if s[j].isalpha():
                print(s[j], end='')
            if s[j].isdigit():
                for m in range(int(s[j])):
                    calculation(s[start[0]+1:end[len(end)-1]])

        for i in range(end[len(end)-1]+1, len(s)):
            if s[i].isalpha():
                print(s[i], end='')


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n-1):
    calculation(string[i])
    print('\r')

calculation(string[n-1])


