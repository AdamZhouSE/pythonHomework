def check(number):
    index=0
    while True:
        if 2**index==number:
            return True
        if 2**index>index:
            break
        index+=1
    return False

import itertools
strs = input()
lists = list(strs)
checks = False
for i in itertools.permutations(lists):
    temp = ''.join(i)
    if temp[0]!='0':
        number = int(temp)
        if check(number):
            checks = True
            break
print("True") if checks else print("False")
