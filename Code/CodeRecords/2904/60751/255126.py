num=input()
sign=0
if num[0]=="-":
    sign=1
    num=num[1:len(num)]
num_l=[]
new=""
begin=0
for i in range(len(num)):
    if new!="":
        begin=1
    if num[-1-i]!="0" or (begin==1 and num[-1-i]=="0"):
        new=new+num[-1-i]
if sign==1:
    new="-"+new
if new=="":
    print(0)
else:
    print(new)
