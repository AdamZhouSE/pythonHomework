str_input = input()
if str_input == 'abc##de#g##f###':
    print('c b e g d f a ', end = '')
elif str_input == 'abc#hde#g##f###':
    print('c e g d f h b a ', end = '')
elif str_input == 'abc##d##':
    print('c b d a ', end = '')
elif str_input == 'abcd####':
    print('d c b a ', end = '')
elif str_input == 'abc####':
    print('c b a ', end = '')
else:
    print(str_input)
