n=list(input())
n=sorted(n)
a="".join(n)
length=len(n)
index=10*(length//3)
if length%3==0:
    index+=7
elif length%3==2:
    index+=4
for i in range(index,index+4):
    num=sorted(list(str(int(2**i))))
    b="".join(num)
    if a==b:
        print(True)
        break
else:
    print(False)