pos=[0,0]
state=1
order=input()*4
for c in order:
    if(c=='G'):
        pos[state%2]+=state-state%2-1
    elif(c=='L'):
        state=(state+1)%4
    elif(c=='R'):
        state=(state-1)%4
print(pos==[0,0])