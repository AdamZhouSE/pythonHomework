str = input()

has_pos_sign = False
has_neg_sign = False
has_dot = False
has_e = False
has_started = False
result = True

for i,s in enumerate(str):
    if s == ' ':
        if has_started:
            if str[i+1] != ' ':
                result = False
                break
    elif s == '.':
        if i == len(str) - 1:
            result = False
            break
        if has_dot or (not has_started) or has_e:
            result = False
            break
        else:
            if not(ord('0')<= ord(str[i+1]) <= ord('9')):
                result = False
                break
            has_dot = True
    elif s == 'e':
        if has_e or (not has_started):
            result = False
            break
        else:
            if i == len(str)-1:
                result = False
                break
            elif not(ord('0')<= ord(str[i+1]) <= ord('9') or str[i+1] == '-'):
                result = False
                break
            has_e = True
    elif s == '+':
        if has_pos_sign or has_started:
            result = False
            break
        else:
            if i == len(str)-1:
                result = False
                break
            if not(ord('0')<= ord(str[i+1]) <= ord('9')):
                result = False
                break
            has_pos_sign = True
            has_started = True
    elif s == '-':
        if has_neg_sign or (str[i-1] != 'e' and has_started):
            result = False
            break
        else:
            if i == len(str)-1:
                result = False
                break
            if not(ord('0')<= ord(str[i+1]) <= ord('9')):
                result = False
                break
            has_neg_sign = True
            has_started = True
    elif ord('0')<= ord(s) <= ord('9'):
        has_started = True
    else:
        result = False
        break

print(result)