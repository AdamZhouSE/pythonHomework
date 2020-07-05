beichushu=int(input())
chushu=int(input())
result=0
fuhao=0
if chushu<0:
    fuhao=fuhao+1
    chushu=-1*chushu
if beichushu<0:
    fuhao=fuhao+1
    beichushu=beichushu*(-1)
while(True):
    if beichushu>=chushu:
        beichushu=beichushu-chushu
        result=result+1
    else:
        break
if fuhao%2==1:
    print(-1*result)
else:
    print(result)