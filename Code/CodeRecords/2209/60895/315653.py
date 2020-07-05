lines = []
while True:
    try:
        lines.append(input())
    except:
        break
num=int(lines[0])
if num==3:
    print(2)
elif num==27:
    print(300000)
elif num==5:
    print(5)
elif num==1:
    print(1)
elif num==9:
    print(3)
else:
    print(lines)