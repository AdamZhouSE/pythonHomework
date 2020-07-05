#zero z 1
#one o 3
#two w 2
#three r 7
#four u 4
#five f 5
#six i 8
#seven v 6
#eight t 9
#nine

strr=input()
list=[]
for i in strr:
    list.append(i)
res=[]
num=0
for i in range(len(list)):
    if list[i]=='z':
        list[i]=' '
        a=0
        b=0
        c=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='e':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='r':
                    list[j]=' '
                    b=1
            if c==0:
                if list[j]=='o':
                    list[j]=' '
                    c=1
for i in range(num):
    res.append(0)
num=0

for i in range(len(list)):
    if list[i]=='w':
        list[i]=' '
        a=0
        b=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='t':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='o':
                    list[j]=' '
                    b=1
for i in range(num):
    res.append(2)
num=0

for i in range(len(list)):
    if list[i]=='u':
        list[i]=' '
        a=0
        b=0
        c=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='f':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='r':
                    list[j]=' '
                    b=1
            if c==0:
                if list[j]=='o':
                    list[j]=' '
                    c=1
for i in range(num):
    res.append(4)
num=0

for i in range(len(list)):
    if list[i]=='o':
        list[i]=' '
        a=0
        b=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='n':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='e':
                    list[j]=' '
                    b=1
for i in range(num):
    res.append(1)
num=0



for i in range(len(list)):
    if list[i]=='f':
        list[i]=' '
        a=0
        b=0
        c=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='i':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='v':
                    list[j]=' '
                    b=1
            if c==0:
                if list[j]=='e':
                    list[j]=' '
                    c=1
for i in range(num):
    res.append(5)
num=0

for i in range(len(list)):
    if list[i]=='v':
        list[i]=' '
        a=0
        b=0
        c=0
        d=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='s':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='e':
                    list[j]=' '
                    b=1
            if c==0:
                if list[j]=='e':
                    list[j]=' '
                    c=1
            if d==0:
                if list[j]=='n':
                    list[j]=' '
                    d=1
for i in range(num):
    res.append(7)
num=0

for i in range(len(list)):
    if list[i]=='r':
        list[i]=' '
        a=0
        b=0
        c=0
        d=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='t':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='h':
                    list[j]=' '
                    b=1
            if c<=2:
                if list[j]=='e':
                    list[j]=' '
                    c+=1
for i in range(num):
    res.append(3)
num=0

for i in range(len(list)):
    if list[i]=='i':
        list[i]=' '
        a=0
        b=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='s':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='x':
                    list[j]=' '
                    b=1
for i in range(num):
    res.append(6)
num=0

for i in range(len(list)):
    if list[i]=='t':
        list[i]=' '
        a=0
        b=0
        c=0
        d=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='e':
                    list[j]=' '
                    a=1
            if b==0:
                if list[j]=='i':
                    list[j]=' '
                    b=1
            if c==0:
                if list[j]=='g':
                    list[j]=' '
                    c=1
            if d==0:
                if list[j]=='h':
                    list[j]=' '
                    d=1
for i in range(num):
    res.append(8)
num=0

for i in range(len(list)):
    if list[i]=='e':
        list[i]=' '
        a=0
        b=0
        num+=1
        for j in range(len(list)):
            if a==0:
                if list[j]=='i':
                    list[j]=' '
                    a=1
            if b<=2:
                if list[j]=='n':
                    list[j]=' '
                    b+=1
for i in range(num):
    res.append(9)
num=0

def bubble_sort(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if int(list[i]) > int(list[j]):
                list[i], list[j] = list[j], list[i]
    return list

res.sort()
strrr=''
for i in res:
    strrr+=str(i)

print(strrr)