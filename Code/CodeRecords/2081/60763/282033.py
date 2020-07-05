s = ''+input()
t = ''+input()
count = 0
for  i in range(len(s)-len(t)+1):
    if t == s[i:i+len(t)]:
        count+=1
print(count,end='')