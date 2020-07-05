n=int(input())
zuihou=0
final=True
for i in range(n):
    chengli=True
    num=[int(n) for n in input().split(",")]
    for index in range(1,len(num)):
        if num[index-1]>=num[index]:
            chengli=False
    if num[0]<=zuihou:
        chengli=False
    if not chengli:
        final=False
        break
if final:
    print("True")
else:
    print("False")