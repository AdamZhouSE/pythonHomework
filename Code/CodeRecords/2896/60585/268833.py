s=input().strip().split(' ')
target=input().strip().split(' ')
num1=[0 for i in range(70)]
num2=[0 for i in range(70)]
for word in s:
    wlen=len(word)
    for i in range(wlen):
        num1[ord(word[i])-65]+=1
for word in target:
    wlen=len(word)
    for i in range(wlen):
        num2[ord(word[i])-65]+=1
isEnough=True
for i in range(70):
    if num1[i]<num2[i]:
        isEnough=False
        break
if isEnough:
    print('YES',end='')
else:
    print('NO',end='')
