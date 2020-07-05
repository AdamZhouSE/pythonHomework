data = input().split(' ')
words = input().split(' ')
total = int(data[0])
res=0
max = int(data[1])
for i in range(0,total):
    count = 0
    for j in range(0,len(words[i])):
        if words[i][j]=='4' or words[i][j]=='7':
            count+=1
    if count<=max:
        res+=1
print(res)
