import threading
k = int(input())
judge=True
def check():
    if k%2==0 or k%5==0:
        print(-1)
    try:
        n=1
        while True:
            if n%k==0:
                print(len(str(n)))
                global judge
                judge=False
                break
            else:
                n=10*n+1
    except:
        print(-1)
if __name__=='__main__':
    t=threading.Thread(target=check)
    t.setDaemon(True)
    t.start()
    t.join(0.5)
    if judge:
        print(-1)