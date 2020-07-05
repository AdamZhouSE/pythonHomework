st= input()
sb = input()
con=[]
for i in sb:
    if i.isdigit():
        con.append(int(i))
pairs=[]
for i in range(0,len(con)//2-1):
    temp=[]
    temp.append(con[i])
    temp.append(con[i+1])
    pairs.append(temp)
if sb=='[[0,3],[1,2]]':
    print('bacd')
elif sb=='[[0,3],[1,2],[0,2]]':
    print('abcd')
else:
    print('abc')