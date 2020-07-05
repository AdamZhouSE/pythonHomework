num=int(input().strip())
for i in range(num):
    line1=input().strip()
    length1=int(line1.split()[0])
    length2=int(line1.split()[1])
    X=int(line1.split()[2])
    s=set([int(x) for x in input().strip().split()])
    t=set([int(x) for x in input().strip().split()])
    for ele1 in s:
        for ele2 in t:
            if ele1+ele2==X:
                print(str(ele1)+' '+str(ele2))
    