s=input()
s=s[1:len(s)-1].split(",")
result=[]
for i in s:
    if s.count(i)>len(s)//3:
        if result.count(int(i))==0:
            result.append(int(i))
print(result)