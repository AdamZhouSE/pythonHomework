count=0
boy=int(input())
numbersboy=list(map(int,input().split(" ")))
girl=int(input())
numbersgirl=list(map(int,input().split(" ")))
for i in range(0,boy):
    minN=100000
    k=-1
    for j in range(0,len(numbersgirl)):
        if abs(numbersgirl[j]-numbersboy[i])<=1:
            if abs(numbersgirl[j]-numbersboy[i])<minN:
                minN=abs(numbersgirl[j]-numbersboy[i])
                k=j
    if k!=-1:
        numbersgirl.remove(numbersgirl[k])
        count=count+1
print(count)