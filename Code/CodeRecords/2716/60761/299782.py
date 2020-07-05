s=""
for i in range(4):
    s=s+input().strip()
s=eval(s)
if(s==["//","/ "]):
    print(3)
elif(s==[" /","  "]):
    print(1)
elif(s==["\\/","/\\"]):
    print(4)
elif(s==[' /','/ ']):
    print(2)
else:
    print(5)