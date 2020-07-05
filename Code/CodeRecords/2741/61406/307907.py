source = input().lstrip('[').rstrip(']').split(',')
length = 1
maxlen = 1
for b in range(0,len(source)-1):
    for a in range(b,len(source)-1):
        if int(source[a])<int(source[a+1]):
            length+=1
        elif int(source[a])>=int(source[a+1]):
            maxlen = max(maxlen,length)
            length=1
print(maxlen)