s=input().split("  ")
p1=int(s[0])
p2=int(s[1])
p3=int(s[2])
st=input().split("-")
result=st[0]
for i in range(3):
    str1=''
    if ord('a')<=ord(st[i][len(st[i])-1])<=ord('z') and ord('a')<=ord(st[i+1][0])<=ord('z'):
        if ord(st[i][len(st[i])-1])<ord(st[1+i][0]):
            if p3==2:
                j=int(ord(st[1+i][0]))-1
                while j>int(ord(st[i][len(st[i])-1])):
                    for k in range(p2):
                        str1=str1+chr(j)
                    j=j-1
            else:
                j=int(ord(st[i][len(st[i])-1]))+1
                while j<int(ord(st[i+1][0])):
                    for k in range(p2):
                        str1=str1+chr(j)
                    j=j+1
            if p1 == 1:
                result = result + str1 + st[i + 1]
            if p1 == 2:
                result = result + str1.upper() + st[i + 1]
            if p1 == 3:
                str2 = ''
                for l in range(len(str1)):
                    str2 = str2 + '*'
                result = result + str2 + st[i + 1]
        else :
            result=result+st[i]+'-'+st[i+1]
    elif ord('0')<=ord(st[i][len(st[i])-1])<=ord('9') and ord('0')<=ord(st[i+1][0])<=ord('9'):
        if ord(st[i][len(st[i])-1])<ord(st[1+i][0]):
            if p3==2:
                j=int(ord(st[1+i][0]))-1
                while j>int(ord(st[i][len(st[i])-1])):
                    for k in range(p2):
                        str1=str1+chr(j)
                    j=j-1
            else:
                j=int(ord(st[i][len(st[i])-1]))+1
                while j<int(ord(st[i+1][0])):
                    for k in range(p2):
                        str1=str1+chr(j)
                    j=j+1
            if p1!=3:
                result=result+str1+st[i+1]
            else:
                str2 = ''
                for l in range(len(str1)):
                    str2 = str2 + '*'
                result = result + str2 + st[i + 1]
        else:
            result=result+st[i]+'-'+st[i+1]
    else :
        result = result+'-'+st[i+1]
print(result)