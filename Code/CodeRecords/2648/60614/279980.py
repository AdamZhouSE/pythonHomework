str=input()
key=input()
while(key in str):
    str=str.replace(key,"")
print(str)