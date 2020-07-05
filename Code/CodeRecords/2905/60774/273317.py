binLst = input()[1:-1].split(',')
binNum = '0b' + ''.join(binLst)
print(int(binNum,2))