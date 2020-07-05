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
    if n<3:
        print(0)
    else:
        list1=list(lines.pop(0).split(" "))
        list1 = list(map(int, list1))
        list1.sort()
        chengji=list1[0]*list1[1]*list1[2]
        for j in range(1,n-2):
            a=int(list1[j])
            for k in range(j+1,n-1):
                b=int(list1[k])
                for l in range(k+1,n):
                    c=int(list1[l])
                    if a*b*c>chengji:
                        chengji=a*b*c
        print(chengji)