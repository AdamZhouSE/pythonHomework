temp=input().split()
n=int(temp[0])
m=int(temp[1])
c=int(temp[2])
seq=input().split()

def muteStart():
    find=False
    for i in range(n-m+1):
        ran=findRan(i,i+m-1)
        if(ran<=c):
            print(i+1)
            find=True
    if(find==False):
        print('NONE',end='')
        
def findRan(x,y):
    large=int(seq[x])
    small=int(seq[x])
    for i in range(x,y+1):
        if(int(seq[i])>large):
            large=int(seq[i])
        if(int(seq[i])<small):
            small=int(seq[i])
    return large-small        

muteStart()