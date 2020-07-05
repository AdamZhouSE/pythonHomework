n = int(input())
string = ''
for i in range(n):
    op, word = input().split(' ')
    if op == 'T':
        string+=word
    elif op == 'U':
        string = string[:len(string)-int(word)]
    elif op == 'Q':
        print(string[int(word)-1])