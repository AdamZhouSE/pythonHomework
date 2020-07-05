import threading
instruction=list(input())
judge=False
point=[0,0]
def check():
    global judge
    mianXiang=0
    try:
        while True:
            for i in instruction:
                if i=='G':
                    if abs(mianXiang%360)==0:
                        point[1]+=1
                    elif abs(mianXiang%360)==90:
                        point[0]+=1
                    elif abs(mianXiang%360)==180:
                        point[1]-=1
                    else:
                        point[0]-=1
                elif i=='L':
                    mianXiang-=90
                elif i=='R':
                    mianXiang+=90
            if point==[0,0]:
                judge=True
                break
    except:
        exit(0)
if __name__=='__main__':
    t=threading.Thread(target=check)
    t.setDaemon(True)
    t.start()
    t.join(0.1)
    print(judge)