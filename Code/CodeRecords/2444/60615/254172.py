num,k,t=map(str,input().split(', '))
num=list(map(int,num.split(' = ')[1].replace('[','').replace(']','').split(',')))
k=int(k.split(' = ')[1])
t=int(t.split(' = ')[1])
start=0
result='true'
step=k+1
while start+k<len(num):
    if num[start]-num[start+k]>t|num[start+k]-num[start]>t:
        result='false'
        break
    start=start+1
start=0
while start+step<len(num):
    if num[start]-num[start+step]<=t|num[start+step]-num[start]<=t:
        result='false'
        break
    step=step+1
print(result)