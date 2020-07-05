s=input()
letter=[]
for i in range(len(s)):
    if not letter.__contains__(s[i]):
        letter.append(s[i])
for i in range(len(s)-1):
    j=i+1
    while j<len(s):

        t=s[i:j+1]
        #看t是否是aaaa或aabb型
        n=1
        for k in range(1,len(t)):
            if t[k]!=t[k-1]:
                n=n+1
            if n>2:
                break
        if n<=2:
            if not letter.__contains__(t):
                letter.append(t)
        j=j+1
print(len(letter))
