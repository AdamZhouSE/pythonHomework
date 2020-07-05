a=input()
b=input()
lena=len(a)
lenb=len(b)
if lena>lenb:
    dif=lena-lenb
    while dif>0:
        b="0"+b
        dif-=1
elif lenb>lena:
    dif=lenb-lena
    lena=lenb
    while dif>0:
        b="0"+b
        dif-=1
        
go="0"
res=""
for i in range(lena-1,-1,-1):
    add=int(a[i])+int(b[i])+int(go)
    if add==3:
        res="1"+res
        go="1"
    elif add==2:
        res="0"+res
        go="1"
    elif add==1:
        res="1"+res
        go="0"
    else:
        res="0"+res
        go="0"
if go=="1":
    res="1"+res
print(res)