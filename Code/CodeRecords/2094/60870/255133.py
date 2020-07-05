import re

str_test = input()
str_test = str_test.replace(' ', '')
if re.match('0', str_test) is not None:
    print('True')
elif re.match(r'^\-?[1-9]+\d*$', str_test) is not None:
    print('True')
elif re.match(r'^(\-?0)|(\-?[1-9]+\d*)\.\d+$', str_test) is not None:
    print('True')
elif re.match(r'^((\-?0)|(\-?[1-9]+\d*)\.\d+)|0|(\-?[1-9]+\d*)e\-?[1-9]+\d*$', str_test) is not None:
    print('True')
else:
    print('False')