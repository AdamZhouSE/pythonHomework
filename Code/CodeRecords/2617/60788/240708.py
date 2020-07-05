from sys import stdin
def cal_one(str):
    return list(str).count('1')


num=int(stdin.readline().strip())
for i in range(0,num):
    line=stdin.readline()
    s1=line.split()[0]
    s2=int(line.split()[1])
    count=0
    for j in range(1,len(s1)+1):
        for k in range(0,len(s1)-j+1):
            part=s1[k:k+j]
            if cal_one(part)==s2:
                count+=1
    print(count)