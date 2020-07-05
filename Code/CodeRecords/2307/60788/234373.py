from sys import stdin

def fre(list):
    s=[list.count(x) for x in list]
    max=0
    for k in range(0,len(s)):
        if s[k]>len(s)/2:
            return list[k]
    return -1

times= stdin.readline().strip()
i=1
while i<=int(times):
    i+=1
    length=stdin.readline().strip()
    list=stdin.readline().split()
    print(fre(list))