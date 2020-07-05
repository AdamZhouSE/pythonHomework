import re
# print(re.match('a(a|cb+)*a', 'acbbbaacb').group())
pattern = input()

while pattern:
    string = input()
    if re.match(pattern, string):
        if re.match(pattern, string).group() == string:
            print('Yes')
        else:
            print("No")
    else:
        print('No')

    pattern = input()