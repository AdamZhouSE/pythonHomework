firstLine=input()
n=int(firstLine)
secondLine=input().split()
if "0" in secondLine:
    print(len(set(secondLine))-1)
else:
    print(len(set(secondLine)))