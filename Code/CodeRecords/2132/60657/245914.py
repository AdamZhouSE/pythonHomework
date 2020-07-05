n=input()
cons=[0,0,0,0,0,0,0,0,0,0]
cons[0]=(n.count('z'))
cons[2]=(n.count('w'))
cons[4]=(n.count('u'))
cons[6]=(n.count('x'))
cons[8]=(n.count('g'))
cons[5]=(n.count('f')-cons[4])
cons[3]=(n.count('h')-cons[8])
cons[7]=(n.count('s')-cons[6])
cons[1]=(n.count('o')-cons[0]-cons[2]-cons[4])
cons[9]=(n.count('i')-cons[5]-cons[6]-cons[8])
st1r=''
words=['zero','one','two','three','four','five','six','seven','eight','nine']
st2r=''
for i in range(10):
    if cons[i]==1:
        st1r+=str(i)
        st2r+=words[i]
print(st1r)