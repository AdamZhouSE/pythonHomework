def is_dec(src):
    havepoint=False
    have_a_e =False
    have_a_e_sign=False
    if not src[0].isdigit():
        return False
    for c in src[1:]:
        if c =='.' and not havepoint:
            havepoint=True
            continue
        elif c == 'e' and not have_a_e:
            have_a_e=True
            continue
        elif (c=='+' or c=='-') and not have_a_e_sign:
            have_a_e_sign=True
            continue
        elif not c.isdigit():
            return False
    return True

src=input()
src=src.replace(' ','')
if src[0]=='+' or src[0]=='-':
    src = src[1:]
print(is_dec(src))
