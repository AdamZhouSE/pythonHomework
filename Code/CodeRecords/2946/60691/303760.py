string = input()
count = 0
pre = string[0]
for x in range(1,len(string)):
    if(string[x] != pre):
        count += 1
        pre = string[x]
    else:
        continue

if(string[len(string)-1] == '0'):
    count += 1
print(count,end='')