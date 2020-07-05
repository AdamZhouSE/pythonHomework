s=input()
t=input()
str=""
for i in s:
    if(i in t):
        str=str+i
for  i in t:
    if(i not in s):
        str=str+i
print(str)
    