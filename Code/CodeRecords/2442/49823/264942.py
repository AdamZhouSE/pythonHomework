def ak(l):
    if len(l)<2:
        print(0)
    else:
        l=sorted(l)
        r=0
        for i in range(1,len(l)):
            r=max(r,l[i]-i[i-1])
        print(r)
if __name__ == '__main__':
    ak(eval(input()))
