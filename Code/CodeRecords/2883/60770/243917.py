def solve():
    rows,colums=map(int,input().split())
    box=[]
    x,x1,x2,y,y1,y2=(0 for i in range(6))
    length=0
    never=True
    for i in range(rows):
        box.append(list(input()))
    for i in range(rows):
        if box[i].count('B')!=0:
            if never:
                y1=box[i].index('B')+1
                box[i].reverse()
                y2=len(box[i])-box[i].index('B')
                x1=i+1
                never=False
            length+=1
    y=int((y1+y2)/2)
    x=x1+int(length/2)
    print(x,y)

if  __name__ == '__main__' :
    solve()


