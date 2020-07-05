arrayString=input()
s=eval(arrayString)
s=list(s)
s.sort()
for i in range(len(s)-3,-1,-1):
    if s[i]+s[i+1]>s[i+2]:
        print(s[i]+s[i+1]+s[i+2])
        break
    