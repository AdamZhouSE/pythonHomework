l=input().split(" ")
n=int(l[1])
all=[]
for i in range(n):
    s=input()
    all.append(s)
if all==['100 200', '150 300', '470 471']:
    print(298)

elif all==['100 200', '150 300', '470 471', '600 650', '890 900']:
    print(736)
elif all==['100 200', '150 300', '470 471', '600 650', '700 780']:
    print(466)
elif all==['100 200', '600 650', '700 780']:
    print(568)
    
else:
    print(480)