s=input().split(",")
for i in range(len(s)): s[i]=int(s[i])
lens=[]
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j+1,len(s)):
            triangle=[s[i],s[j],s[k]]
            triangle.sort()
            if triangle[1]+triangle[0]>triangle[2]:
                lens.append(triangle[1]+triangle[0]+triangle[2])
if len(lens)==0: print(0)
else: print(max(lens))