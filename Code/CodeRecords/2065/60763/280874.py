word = str(input())
word = word[1:len(word)-1]
isNum = True
str1 = '0123456789'
for i in range(len(word)):
    if(str1.find(word[i])!=-1 and ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z')):
        isNum = False
        break
if isNum:
    if word.find(' ') != -1:
        a = int(word[0:word.find(' ')-1])
    else:
        a = int(word)
    if a >= 0:
        print(min(pow(2,31)-1,a))
    else:
        print(max(-pow(2, 31), a))
else:
    print(0)
a = int(word[0:word.find(' ')])