s = ''+input()
t = ''+input()
count = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j] in t:
            for k in range(len(t)-(j-i)+1):
                if s[i:j] == t[k:k+j-i]:
                    count+=1
print(count)