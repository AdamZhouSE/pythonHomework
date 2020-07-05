str=input()
key=input()
while(key in str):
    str=str.replace(key,"")
if str!="":
    print(str,end="")
else:
    print(key,end="")