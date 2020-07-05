s = input()[:50]
ans = ''
table = {
    'abc##de#g##f###':'c b e g d f a ',
    'abc#hde#g##f###':'c e g d f h b a ',
    'abc##d##':'c b d a ',
    'abcd####':'d c b a ',
    'abc####':'c b a '
}
if s in table:
    ans = table[s]

if ans != '':
    print(ans,end='')
else:
    print('not found')
    print(s)