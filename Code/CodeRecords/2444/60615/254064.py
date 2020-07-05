num,k,t=map(str,input().split(', '))
num=list(map(int,num.split(' = ')[1].replace('[','').replace(']','').split(',')))
k=int(k.split(' = ')[1])
t=int(t.split(' = ')[1])
start=0
result='false'
while start+k<len(num):
    if num[start]-num[start+k]==t|num[start+k]-num[start]==t:
        result='true'
        break
    start=start+1
print(result)