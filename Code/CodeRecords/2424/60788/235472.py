from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    s=[int(x) for x in stdin.readline().split()]
    for element in s:
        if s.count(element)%2!=0:
            print(element)
            break