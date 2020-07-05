def get_reverse(ch):
    if ord('a') <= ord(ch) <= ord('z'):
        return chr(ord('z') + ord('a') - ord(ch))
    elif ord('A') <= ord(ch) <= ord('Z'):
        return chr(ord('Z') + ord('A') - ord(ch))
    else:
        return ch

s = input()
while s != '!':
    print(''.join([get_reverse(i) for i in list(s)]))
    s = input()