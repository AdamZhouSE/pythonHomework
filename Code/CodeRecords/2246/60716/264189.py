def check(number):
#    print(number)
    index=0
    while True:
#        print(index)
        if 2**index==number:
            return True
        if 2**index>number:
            break
        index+=1
    return False

import itertools
strs = input()
lists = list(strs)
checks = False
for i in itertools.permutations(lists):
    temp = ''.join(i)
#    print(temp)
    if temp[0]!='0':
        number = int(temp)
        if check(number):
            checks = True
            break
print("True") if checks else print("False")
