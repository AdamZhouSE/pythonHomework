n = input()
li = n.split(',')
if int(li[3])-int(li[1])>=0 and int(li[0])-int(li[2])>=0:
    print('True')
else:
    print('False')