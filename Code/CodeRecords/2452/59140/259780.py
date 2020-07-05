row=int(input())
str=''
for i in range(row):
    str+=input()
    str+=","
str=str[:len(str)-1].split(',')
target=input()
if str.count(target)!=0:print(True)
else:print(False)