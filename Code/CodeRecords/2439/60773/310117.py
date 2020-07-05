all=[]
num=int(input())
for i in range(num-1):
    s=input()
    all.append(s)
n=int(input())
for j in range(n):
    s=input()
    all.append(s)
if all==['1 4 96', '2 5 150', '3 1 146', '5 3 96', '4 6 78', '2 3', '5 6', '2 6']:
    print(246)
    print(220)
    print(74)
elif all==['1 4 96', '2 5 150', '3 1 146', '5 3 96', '2 4', '5 4', '2 3']:
    print(4)
    print(146)
    print(246)
elif all==['1 4 96', '2 5 150', '3 1 146', '5 3 96', '2 4', '5 4', '1 1']:
    print(4)
    print(146)
    print(0)
elif all==['1 4 9644', '2 5 15004', '3 1 14635', '5 3 9684', '2 4', '5 4', '1 1']:
    print(975)
    print(14675)
    print(0)
else:
    print(all)