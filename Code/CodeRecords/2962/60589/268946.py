np=input().split(' ')
n=int(np[0])
p=int(np[1])
strs=input().split(' ')
taken=[]


def allocate(s):
    return ((ord(s[0])-ord('A'))*(32**2)+(ord(s[1])-ord('A'))*32+ord(s[2])-ord('A'))%p


def probe(num):
    i=0
    while True:
        if (num+i**2)%p not in taken:
            taken.append((num+i**2)%p)
            return 
        elif (num-i**2)%p not in taken:
            taken.append((num - i ** 2) % p)
            return
        i+=1


for s in strs:
    probe(allocate(s[-3:]))
taken=list(map(str,taken))
print(' '.join(taken))