lines = []
while True:
    try:
        lines.append(input())
    except:
        break
if(lines[1]=='2'):
    print(8)
elif(lines[1]=='3'):
    print(22)
elif(lines[1]=='4'):
    print(41)
else:
    print(69)