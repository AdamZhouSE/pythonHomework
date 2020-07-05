xStr=input()
x=float(xStr)
n=int(input())
res=x**n
resStr=str(res)
count=0
point=0
for index in range(len(resStr)):
    if resStr[index]=='.':
        count=len(resStr)-index-1
        point=index

for i in range(5-count):
    resStr=resStr+'0'
if count>5:
    resStr=resStr[:point+6]
print(resStr)
