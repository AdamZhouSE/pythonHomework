string = input()
ST = int(input())
newString = '';
for i in string:
    newString += (str(ord(i)-ord('A')+ST))


while len(newString) > 2 and newString is not '100':
    tmp = ''
    for index in range(len(newString)-1):
        templeNumber = int(newString[index]) + int(newString[index+1])
        templeNumber = templeNumber % 10
        tmp = tmp + str(templeNumber)
    newString = tmp
print(int(newString),end="")
    
    