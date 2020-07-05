n=int(input())
ghosts=[]
for i in range(n):
    ghosts.append(eval('['+input()+']'))
target=eval('['+input()+']')
def man(ac1,ac2):
    return abs(ac1[0]-ac2[0])+abs(ac1[1]-ac2[1])
dis=man([0,0],target)
j=0
for i in ghosts:
    if(man(i,target)<=dis):
        print("False")
        j=1
        break
if(j==0):
    print("True")