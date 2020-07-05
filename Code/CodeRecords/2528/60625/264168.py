listStr=input()
listStr=listStr[1:len(listStr)-1]
list=listStr.split(',')
list.sort()
print('['+', '.join(list)+']')