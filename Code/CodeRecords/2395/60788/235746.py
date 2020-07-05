from sys import stdin 

def operate(list,p):
    if list[p+1]!=0 and list[p+1]==list[p] :
        list[p]*=2
        list[p+1]=0
        resort(list)
        
def resort(list):
    
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline())
    list=[int(x) for x in stdin.readline().split()]
    for j in range(0,length):
        operate(list,j)
        