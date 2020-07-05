s=[int(x) for x in eval(input())]
count=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]>2*s[j]:
            count+=1
print(count)