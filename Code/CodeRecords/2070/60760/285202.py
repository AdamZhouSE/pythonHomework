s=input()
a=float(s)
l=len(s)-s.find('.')
b=int(input())
res=pow(a,b)
strres=str(res)
while len(strres)-strres.find('.')<l:
    strres=strres+'0'
if len(strres)-strres.find('.')>l:
    strres=strres[0:strres.find('.')+l]
print(strres)
