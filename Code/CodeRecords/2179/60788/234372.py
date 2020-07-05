from sys import stdin
def trans(list):
    return 'a'*int(list[0])+'b'*int(list[1])+'c'*int(list[2])+'d'*int(list[3])

line=stdin.readline()
length1=int((line.split())[0])
length2=int(line.split()[1])
str=stdin.readline().strip()
for i in range(0,length2):
    str2=trans(stdin.readline().split())
    k=0
    while str2[k]==str[k]:
        k+=1
    print(k)