s=input()
num=0
for i in range(len(s)):
    if(s[i]=="A"):
        num+=s[:i].count("Q")*s[i:].count("Q")
print(num,end="")