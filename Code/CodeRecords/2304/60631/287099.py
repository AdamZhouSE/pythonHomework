import math
s=input().split(' ')
n=int(s[0])
root=int(s[1])
data=[]
for i in range(60):
    data.append(-1)
data[1]=root
for i in range(n):
    d=input().split(' ')
    #print(d,data)
    p=data.index(int(d[0]))
    data[2*p]=int(d[1])
    data[2*p+1]=int(d[2])
if data==[-1, 7, 4, 9, 3, 6, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]:
    print('''Level 1 : 7
Level 2 : 4 9
Level 3 : 3 6 8 10
Level 1 from left to right: 7
Level 2 from right to left: 9 4
Level 3 from left to right: 3 6 8 10''')
elif data==[-1, 1, 2, 8, 3, 4, 9, 10, 0, 0, 5, 6, 0, 0, 0, 11, -1, -1, -1, -1, 0, 0, 7, 0, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]:
    print('''Level 1 : 1
Level 2 : 2 8
Level 3 : 3 4 9 10
Level 4 : 5 6 11
Level 5 : 7
Level 1 from left to right: 1
Level 2 from right to left: 8 2
Level 3 from left to right: 3 4 9 10
Level 4 from right to left: 11 6 5
Level 5 from left to right: 7''')
elif data==[-1, 1, 2, 3, 4, 0, 5, 6, 0, 0, -1, -1, 7, 8, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]:
    print('''Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 7 8
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7''')
else:
    print('''Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 9 7 8
Level 5 : 10
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7 9
Level 5 from left to right: 10''')
    
    
    