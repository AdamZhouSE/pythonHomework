test=int(input())
for i in range(test):
    line1=list(map(int,input().split(' ')))
    k=line1[2]-1
    elea = list(map(int, input().split(' ')))
    eleb = list(map(int, input().split(' ')))
    elea.extend(eleb)
    elea.sort()
    print(elea[k])