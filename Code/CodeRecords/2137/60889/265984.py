num = int(input())
summary = 0
for i in range(1,int((num/2)+1)):
    if (num%i)==0:
        summary = summary + i
if summary == num:
    print(True)
else:
    print(False)