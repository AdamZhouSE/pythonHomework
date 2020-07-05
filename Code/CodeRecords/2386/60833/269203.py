lines = []
while True:
    try:
        lines.append(input())
    except:
        break
count=int(lines.pop(0))
for i in range(0,count):
    number=0
    n=int(lines.pop(0))
    if n<4:
        print(0)
    else:
        list1=list(lines.pop(0).split(" "))
        list1 = list(map(int, list1))
        list1.sort()
        target=int(lines.pop(0))
        for j in range(0,n-3):
            a=int(list1[j])
            for k in range(j+1,n-2):
                b=int(list1[k])
                for l in range(k+1,n-1):
                    c=int(list1[l])
                    for m in range(l+1,n):
                        d=int(list1[m])
                        if a+b+c+d==target:
                            number=1
        print(number)