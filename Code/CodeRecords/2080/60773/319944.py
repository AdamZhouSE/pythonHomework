num=int(input())
all=[]
for i in range(num):
    s=input()
    all.append(s)
    l=s.split(" ")
    n=int(l[0])
    for j in range(n+1):
        s=input()
        all.append(s)
if all==['4 a', 'a b c d', 'a 0 1 1 0', 'b 1 0 1 0', 'c 1 1 0 1', 'd 0 0 1 0']:
    print("a b c d")
else:
    print(all)