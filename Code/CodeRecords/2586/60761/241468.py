abc=[]
moves=[]
for i in range(3):
    abc.append(int(input("")))
abc.sort()
if abc[0]+1==abc[1] and abc[1]+1==abc[2]:
    minimum_moves=0
elif abc[1]-abc[0]<=2 or abc[2]-abc[1]<=2:
    minimum_moves=1
else:
    minimum_moves=2
moves.append(minimum_moves)
maximum=abc[2]-abc[0]-2
moves.append(maximum)
print(moves)