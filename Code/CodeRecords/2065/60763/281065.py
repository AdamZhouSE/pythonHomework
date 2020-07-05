word = str(input())
# word = word[1:len(word)-1]
# print(word)
isNum = True
str1 = '0123456789'
fstN = -1
lastN = -1
for i in range(len(word)):
    if not word[i] in str1 and word[i] != ' ' and not (word[i] == '+' or word[i] == '-'):
        isNum = False
        break
    if word[i] in str1 or word[i] == '+' or word[i] == '-':
        fstN = i
        break
i = fstN+1
while i < len(word):
    if not (word[i] in str1):
        break
    lastN =i
    i+=1
if fstN == -1:
    isNum = False
# else:
#     i = fstN
#     while i < len(word):
#         if (str1.find(word[i]) != -1 and ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z')):
#             isNum = False
#             break
#     for i in range(len(word)):
#         if (str1.find(word[i]) != -1 and ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z')):
#             isNum = False
#             break
if isNum:
    # if word.find(' ') != -1:
    #     a = int(word[0:word.find(' ')-1])
    # else:
    #     a = int(word)
    a = int(word[fstN:lastN+1])
    if a >= 0:
        print(min(pow(2,31)-1,a))
    else:
        print(max(-pow(2, 31), a))
else:
    print(0)