def Test():
    num=int(input())
    learn=eval(input())
    how=[]
    count=1
    i=0
    how.append(find(learn))
    while(count<num):
        if(how.count(learn[i][1])!=0):
            how.append(learn[i][0])
            count=count+1
            learn.remove(learn[i])
            i=0
        else:
            i=i+1
    print(how)

def find(learn):
    ban=[]
    for i in range(0,len(learn)):
        ban.append(learn[i][0])
    for i in range(0,len(learn)):
        if(ban.count(learn[i][1])==0):
            return learn[i][1]
if __name__ == "__main__":
    Test()