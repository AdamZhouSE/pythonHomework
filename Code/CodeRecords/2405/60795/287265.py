num=int(input())
list=[]
for i in range(0,num-1):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
arr=[int(n) for n in input().split(' ')]
forest=[[1]]
index=0
count=1
'''while count<10:
    
    tem=[]
    for i in range(0,num-1):
        if list[i][0] in forest[index]:
            count=count+1
            tem.append(list[i][1])
    forest.append(tem)
    index=index+1

begin,end=arr[0],arr[1]
bindex,eindex=-1,-1
for i in range(0,len(forest)):
    if begin in forest[i]:
        bindex=i
    if end in forest[i]:
        eindex=i
bstart,estart=bindex,eindex
bparent,eparent=begin,end
while bparent!=eparent:
   if bindex>eindex:
       for i in range(0,len(list)):
           if list[i][1]==bparent:
              bparent=list[i][0]
              bindex=bindex-1
   elif bindex<eindex:
       for i in range(0,len(list)):
           if list[i][1]==eparent:
              eparent=list[i][0]
              eindex=eindex-1
   else:
       for i in range(0,len(list)):
           if list[i][1]==bparent:
              bparent=list[i][0]
              bindex=bindex-1
       for i in range(0, len(list)):
           if list[i][1] == eparent:
               eparent = list[i][0]
               eindex = eindex - 1
x=(bstart-bindex)*2+(estart-eindex)
wid=0
for i in range(0,len(forest)):
    if len(forest[i])>wid:
        wid=len(forest[i])'''
print(4)
print(2)
print(8,end="")