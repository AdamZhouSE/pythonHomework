the_num = input()
for i in range(0, len(the_num)):
    if the_num[i] == '6':
        the_num = the_num[0:i] + '9' + the_num[i+1:]
        break
print(the_num)