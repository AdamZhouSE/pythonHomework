def compare(s1,s2):
    for i in range(0,len(s1)):
        end=s1[i:len(s1)]
        if s2.endswith(end):
            return len(end)
    return 0

line1=list(map(int,input().split(' ')))
line2=input()
length=line1[0]
num=line1[1]

for i in range(0,num):
    line3=list(map(int,input().split(' ')))
    l=line3[0]-1
    r=line3[1]-1
    max=0
    for j in range(l,r+1):
        s1=line2[0:j+1]
        for k in range(j+1,r+1):
            s2=line2[0:k+1]
            if max<compare(s1,s2):
                max=compare(s1,s2)
    print(max)
        