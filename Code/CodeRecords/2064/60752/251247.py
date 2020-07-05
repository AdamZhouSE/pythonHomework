roman=input()
IV4=roman.find('IV')!=-1
IX9=roman.find('IX')!=-1
XL40=roman.find('XL')!=-1
XC90=roman.find('XC')!=-1
CD400=roman.find('CD')!=-1
CM900=roman.find('CM')!=-1
add=0
for r in list(roman):
    if r=='I':add+=1
    if r=='V':add+=5
    if r=='X':add+=10
    if r=='L':add+=50
    if r=='C':add+=100
    if r=='D':add+=500
    if r=='M':add+=1000
if IV4:add-=2
if IX9:add-=2
if XL40:add-=20
if XC90:add-=20
if CD400:add-=200
if CM900:add-=200
print(add)