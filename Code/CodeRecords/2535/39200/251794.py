string=input();
A=string[1:-1:1].split(',')
D=[]
it=iter(A)
for x in it:
    D.append(int(x))
    
start=0
end=len(D)-1
blocks=0
#print(D)

if(D[start]>D[end]):
    print(1)
else:
    end-=1
    while(end!=len(D)):
        end=len(D)-1
        if end!=start:
            while D[start]<=D[end]:
                end-=1
                if(end==start):
                    break
        #print(D[end])
        start=end+1
        #print(D[start])
        blocks+=1
        if(start==len(D)):
            break
    print(blocks)