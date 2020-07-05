from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    leaders=int(stdin.readline().strip())
    temp=stdin.readline().split()
    ability=[int(x) for x in temp]
    length=len(ability)
    max=ability[0]*ability[1]*ability[2]
    for j in range(0,length-2):
        for k in range(j+1,length-1):
            for l in range(k+1,length):
                mult=ability[j]*ability[k]*ability[l]
                if mult>max:
                    max=mult
    print(max)