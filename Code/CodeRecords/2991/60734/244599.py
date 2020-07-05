def reverse(string):
    string = list(string)
    res = ''
    for i in range(len(string)):
        if string[len(string)-i-1]!=' ':
            res+=string[len(string)-i-1]
    return res

string = input()
print(reverse(string),end = " ")