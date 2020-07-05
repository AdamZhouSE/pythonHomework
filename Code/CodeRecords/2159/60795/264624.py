dict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
num=int(input())
new=[]
result=""
th,hu,de,fa=0,0,0,0
if num<10:
    fa=num
elif num>=10 and num<100:
    fa=num%10
    de=num//10
elif num>=100 and num<1000:
    hu=num//100
    de=num%100//10
    fa=num%100%10
elif num>=1000 and num<10000:
    th=num//1000
    hu=num%1000//100
    de=num%1000%100//10
    fa=num%1000%100%10
while th>0:
    new.append(dict[1000])
    th=th-1
while hu>0:
    if hu==9:
        new.append(dict[100])
        new.append(dict[1000])
        hu=hu-9
    elif hu>5:
        new.append(dict[500])
        hu=hu-5
    elif hu==4:
        new.append(dict[100])
        new.append(dict[500])
        hu=hu-4
    else:
        new.append(dict[100])
        hu=hu-1
while de>0:
    if de==9:
        new.append(dict[10])
        new.append(dict[100])
        de=de-9
    elif de==4:
        new.append(dict[10])
        new.append(dict[50])
        de=de-4
    elif de>5:
        new.append(dict[50])
        de=de-5
    else:
        new.append(dict[10])
        de=de-1
while fa>0:
    if fa==9:
        new.append(dict[1])
        new.append(dict[10])
        fa=fa-9
    elif fa==4:
        new.append(dict[1])
        new.append(dict[5])
        fa=fa-4
    elif fa>5:
        new.append(dict[5])
        fa=fa-5
    else:
        new.append(dict[1])
        fa=fa-1
result=result.join(new)
print(result)



