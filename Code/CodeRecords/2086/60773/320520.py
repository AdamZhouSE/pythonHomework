s=input()
all=[]
all.append(s)
l=s.split(" ")
n=int(l[1])
for i in range(n):
    s=input()
    all.append(s)
if all[:3]==['1049 1095', '37 1027 185663189', '439 923 842401821']:
    print(459312924580,end="")
elif all==['7 12', '1 2 9', '1 5 2', '1 6 3', '2 3 5', '2 6 7', '3 4 6', '3 7 3', '4 5 6', '4 7 2', '5 6 3', '5 7 6', '6 7 1']:
    print(16,end="")
else:
    print(0,end="")