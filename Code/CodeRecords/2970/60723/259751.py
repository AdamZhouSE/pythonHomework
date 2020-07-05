import re
temp=input()
try:
    array=[]
    while temp!='':
        pattern=temp
        string=input()
        array.append([pattern,string])
        temp=input()
except Exception:
    m=0
for item in array:
    pattern=item[0]
    string=item[1]
    search=re.match(pattern,string)
    if search and len(search.group())==len(string):
        print("Yes")
    else:
        print("No")