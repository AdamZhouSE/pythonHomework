num,k,t=map(str,input().split(', '))
num=list(map(int,num.split(' = ')[1].replace('[','').replace(']','').split(',')))
k=int(k.split(' = ')[1])
t=int(t.split(' = ')[1])
start=0
result='false'
step=1
while step<=k and start+step<len(num):

    while start+step<len(num):
        if num[start]-num[start+step]>t or num[start+step]-num[start]>t:

            break
        start=start+1
        if start+step>=len(num):
            result='true'

    if result=='true':
        break
    start = 0
    step=step+1
print(result)