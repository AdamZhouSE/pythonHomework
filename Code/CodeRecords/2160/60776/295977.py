beichushu=int(input())
chushu=int(input())
result=0
while(True):
    if beichushu>=chushu:
        beichushu=beichushu-chushu
        result=result+1
    else:
        break
print(result)