s = input().split(' ')
print(s)
length = 0
res = ''
for item in s:
    if(len(item)>length):
        length = len(item)
        res = item
print(res)




