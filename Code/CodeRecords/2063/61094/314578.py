s = input()
l = len(s)
judge = True
for i in range(0,l):
    if(s[i]!=s[l-i-1]):
        judge = False
print(judge)