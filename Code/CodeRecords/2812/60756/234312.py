firstLine=input()
secondLine=input().split()
if '0' in secondLine:
    print(len(sorted(set(secondLine)))-1)
else:
    print(len(sorted(set(secondLine))))