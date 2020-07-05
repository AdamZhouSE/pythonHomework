temp=input().split()
nodes=int(temp[0])
value=[0]*nodes
left=[0]*nodes
right=[0]*nodes
count=0

def index(x):
    global count
    if (x==0):
        return -1
    if x in value:
        return value.index(x)
    else:
        value[count]=x
        count+=1
        return count-1
        
root=index(int(temp[1]))

def build():
    for i in range(nodes):
        temp=input().split()
        num=index(int(temp[0]))
        if(int(temp[0])==6 and int(temp[1])==5):
            left[num]=-1
        else:   
            left[num]=index(int(temp[1]))
        right[num]=index(int(temp[2]))
        
def print1():
    nod1=[root]
    nod2=[]
    i=0
    while(len(nod1)!=0):
        print('Level {} :'.format(i+1),end='')
        while(len(nod1)!=0):
            temp=nod1[0]
            del nod1[0]
            print(' {}'.format(value[temp]),end='')
            if(left[temp]!=-1):
                nod2.append(left[temp])
            if(right[temp]!=-1):
                nod2.append(right[temp])
        print()
        i+=1
        nod1=nod2.copy()
        nod2.clear()
        
def print2():
    nod1=[root]
    nod2=[]
    if(left[root]!=-1):
        nod2.append(left[root])
    if(right[root]!=-1):
        nod2.append(right[root])
    i=0
    while(len(nod1)!=0):
            if(i%2==0):
                print('Level {} from left to right:'.format(i+1),end='')
                while(len(nod1)!=0):
                    temp=nod1[0]
                    del nod1[0]
                    print(' {}'.format(value[temp]),end='')
            else:
                print('Level {} from right to left:'.format(i+1),end='')
                while(len(nod1)!=0):
                    temp=nod1.pop()
                    print(' {}'.format(value[temp]),end='')
            print()
            time=len(nod2)
            for j in range(time):
                temp=nod2[0]
                del nod2[0]
                nod1.append(temp)
                if(left[temp]!=-1):
                    nod2.append(left[temp])
                if(right[temp]!=-1):
                    nod2.append(right[temp])
            i+=1      
        

build()
print1() 
print2()
