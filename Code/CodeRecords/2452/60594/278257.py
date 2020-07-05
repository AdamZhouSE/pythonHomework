n=int(input())
zuihou=0
final=True
zc=[]
for i in range(n):
    chengli=True
    num=[int(n) for n in input().split(",")]
    zc.append(num)
    for index in range(1,len(num)):
        if num[index-1]>=num[index]:
            chengli=False
    if num[0]<=zuihou:
        chengli=False
    if not chengli:
        final=False
        break
a=int(input())
cunzai=False
for i in zc:
    if a in i:
        cunzai=True
if final and cunzai:
    print("True")
else:
    print("False")