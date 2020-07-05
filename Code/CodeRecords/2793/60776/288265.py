time=int(input().split()[1])
b=input().split(' ')
for i in range(0, len(b)):
    b[i] = int(b[i])
geshu=0
for i in range(0,len(b)-1):
    if b[i+1]-b[i]>time:
        geshu=0
    else:
        geshu=geshu+1
geshu=geshu+1
print(geshu)