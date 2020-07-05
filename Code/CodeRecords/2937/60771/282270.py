#03
tar = "CODEFESTIVAL2016"
s = input()
count = 0
for i in range(0,len(tar)):
    if s[i] != tar[i]:
        count += 1
print(count)