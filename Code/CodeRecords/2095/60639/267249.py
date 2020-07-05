def addition(string1,string2):
    c=0
    result=''
    n=len(string1)
    for i in range(n):
        x=int(string1[n-1-i])
        y=int(string2[n-1-i])
        s=x^y^c
        result=str(s)+result
        c=(x&c)|(y&c)|(x&y)
    if c==1:
        result='1'+result
    return result
def adjustment(n,string):
    for i in range(n):
        string='0'+string
    return string

string1=input()
string2=input()
diff=abs(len(string1)-len(string2))
if diff!=0:
    if len(string1)<len(string2):
        string1=adjustment(diff,string1)
    else:
        string2=adjustment(diff,string2)
print(addition(string1,string2))
