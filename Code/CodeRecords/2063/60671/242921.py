str1=input()
length=len(str1)
isSame=True
for i in range(length):
    if(str1[i]!=str1[length-1-i]):
        isSame=False
print(isSame)