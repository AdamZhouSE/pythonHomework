str0=input()
count=0
str1='CODEFESTIVAL2016'
for i in range(16):
    if str0[i]!=str1[i]:
        count+=1
print(count)