import string
lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    str1=lines.pop(0)
    temp = []
    for c in str1:
        if c not in string.punctuation:
            if c!=" ":
                temp.append(c)
    newText = ''.join(temp)
    newText=newText.lower()
    newText1=newText[::-1]
    if(newText==newText1):
        print("YES")
    else:
        print("NO")
