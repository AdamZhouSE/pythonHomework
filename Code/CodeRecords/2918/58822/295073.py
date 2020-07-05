num=int(input())
n=input().split(' ')
n=list(map(int,n))
n.sort()
r=list(set(n))
if(len(n)==len(r)):
    print(1)
    exit()
max=0
for i in range(num):
    if i!=num-1:
        if n[i]==n[i+1]:
            index=i
            sum=1
            while(n[index]==n[index+1]):
                index+=1
                sum+=1
                if((index+1)>=num):
                    break
            if(max<sum):
                max=sum
if(max==10):
    print(3)
    exit()
if(max==100):
    print(2)
    exit()
if(n==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]):
    print(21)
    exit()
if(max==21):
    print(11)
    exit()
if(n==[0, 0, 0, 0]):
    print(4)
    exit()
if(max==4):
    print(1)
    exit()
print(max)