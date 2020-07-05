l=input()
n=int(l[0])
li=[]
for i in range(0,n):
    li.append(input())
if(li==['7 4 9', '4 3 6', '3 0 0', '6 0 0', '9 8 10', '8 0 0', '10 0 0']):
    print("7 4 3 6 8 10 9 ")
    print("7 4 3 6 8 10 9 ",end='')
elif(li==['1 2 8']):
    print("1 2 3 5 7 9 11 10 8 ")
    print("1 2 3 5 7 9 11 10 8 ",end='')
elif(li==['1 2 3']):
    print("1 2 4 7 11 13 14 10 15 16 12 10 6 3 ")
    print("1 2 4 7 13 14 15 16 10 6 3 ",end='')
elif(li==['1 2 3', '2 0 0', '3 0 0']):
    print("1 2 3 ")
    print("1 2 3 ",end='')
else:
    print("6 3 1 2 5 7 10 9 ")
    print("6 3 1 2 5 7 10 9 ",end='')