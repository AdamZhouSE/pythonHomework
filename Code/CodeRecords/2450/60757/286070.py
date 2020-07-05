li=list(eval(input()))
t=int(input())
if li.count(t)==0:
    print('[-1, -1]')
else:
    lh=li[::-1]
    print('['+str(li.index(t))+', '+str(len(li)-1-lh.index(t))+']')