string_num=(int)(input())
strings=[]
for i in range(string_num):
    strings.append(input())
minstr=strings[0]
for i in strings:
    if(len(i)<len(minstr)):
        minstr=i
substr=[]
def get_substr(string,n):
    global substr,minstr
    if(n==len(minstr)):
        substr.append(string)
    else:
        get_substr(string,n+1)
        get_substr(string+minstr[n],n+1)

get_substr("",0)
list.sort(substr,key=lambda i:len(i),reverse=True)
for i in substr:
    judge=True
    for j in strings:
        if i not in j:
            judge=False
            break
    if(judge):
        print(len(i))
        break

