import re
while True:
    s1=""
    s2=""
    try:
        s1=input()
        s2=input()
    except:
        break
    if re.match(s1,s2)==None:
        print("No")
    elif re.match(s1,s2).span()!=(0,len(s2)):
        print("No")
    else:
        print("Yes")