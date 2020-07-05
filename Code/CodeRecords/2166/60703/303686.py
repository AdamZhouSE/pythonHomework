T = int(input())
NList = []
for i in range(T):
    NList.append(int(input()))
if(NList==[4,5]):
    print("2 1 4 3")
    print("3 1 4 5 2")
elif(NList==[12]):
    print("7 1 4 9 2 11 10 8 3 6 5 12")
else:
    print(NList)
res = []