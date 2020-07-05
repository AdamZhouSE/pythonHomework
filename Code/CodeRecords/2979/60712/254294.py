s = input().split()
maxlength=0
maxindex=0
for i in range(len(s)):
    if len(s[i])>maxlength:
        maxlength=len(s[i])
        maxindex=i
print(s[maxindex])  