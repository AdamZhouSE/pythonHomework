string = input()
cnt = 0
pre = string[0]
for x in range(1,len(string)):
    if(string[x] != pre):
        cnt += 1
        pre = string[x]
    else:
        continue

if(string[len(string)-1] == '0'):
    cnt += 1
print(cnt,end = "")