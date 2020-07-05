
s=input()
index=0
rs=''
while index<len(s):
    if rs is ''and s[index] is ' ':
        index+=1
    if rs is '' and not s[index].isnumeric() and s[index]!='-' and s[index]!='+' and s[index]!=' ':
        break
    if rs is not'' and not s[index].isnumeric():
        break
    if (rs is '' and (s[index]=='-' or s[index]=='+')) or ((rs is '' or rs.isnumeric() or rs.find('+')!=-1 or rs.find('-')!=-1)and s[index].isnumeric()):
        rs+=s[index]
        index+=1

check=rs
negative=False
int_max='2147483647'
int_min='-2147483648'
if rs is not '':
    if rs[0]=='+':
        check=check[1:]
    if rs[0]=='-':
        negative=True
        check=check[1:]
    if len(check)>10:
        if negative:
            rs=int_min
        else:rs=int_max
    if len(check)==10:
        overflow=False
        if negative:
            for i in range(1,11):
                if check[i-1]>int_min[i]:
                    overflow=True
                    break
        else:
            for i in range(10):
                if check[i]>int_max[i]:
                    overflow=True
                    break
        if overflow:
            if negative:rs=int_min
            else:rs=int_max
if rs is'':rs='0'
print(int(rs))
