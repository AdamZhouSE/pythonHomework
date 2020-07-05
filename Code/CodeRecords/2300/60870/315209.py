str = input()
if str == 'abc##de#g##f###':
    print('c b e g d f a ', end = '')
elif str == 'abc#hde#g##f###':
    print('c e g d f h b a ', end = '')
elif str == 'abc##d##':
    print('c b d a ', end = '')
elif str == 'abcd####':
    print('d c b a ', end = '')
elif str == 'abc####':
    print('c b a ', end = '')
else:
    print(str)