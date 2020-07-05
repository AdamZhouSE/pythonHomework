n,x0,y0=map(int,input().split(' '))
position=[]
def calculate_line(x0,y0,x1,y1):
    if(x0==x1):
        parameter=[1,0,-x0]
    elif(y0==y1):
        parameter=[0,1,-y0]
    else:
        parameter=[y1-y0,x0-x1,y0*(x1-x0)-x0*(y1-y0)]
    return parameter

for i in range(n):
    temp=list(map(int,input().split(' ')))
    position.append(temp)
sum=0
while(len(position)!=0):
   sum+=1
   x1=position[0][0]
   y1=position[0][1]
   parameter=calculate_line(x0,y0,x1,y1)
   temp=[]
   for j in range(len(position)):
       x2=position[j][0]
       y2=position[j][1]
       if(parameter[0]*x2+parameter[1]*y2+parameter[2]!=0):
           temp.append(position[j])
   position=temp
print(sum)