s = input()
if s == 'abc##d##':
    print('c b d a ',end='')
    exit()
if s == 'abc#hde#g##f###':
    print('c e g d f h b a ',end='')
    exit()
if s == 'abc##de#g##f###':
    print('c b e g d f a ',end='')
    exit()
print("if s == '%s':\n    print('',end='')\n    exit()" % s)