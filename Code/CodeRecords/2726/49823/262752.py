def ad(l):
    if len(l) == 0 or l[0] == 'null':
        print(0)
    for i in range(len(l)):
        if l[i]!='null' and (2*i+1>=len(l) or l[2*i+1]=='null') and (2*i+2>=len(l) or l[2*i+2]=='null'):
            h=1
            while i>0:
                i=(i-1)//2
                h+=1
            print(h)
            return
if __name__ == '__main__':
    ad([i for i in input()[1:-1].split(',')])
