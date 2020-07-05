All= int(input())

for q in range(0,All):
    string=input()
    length=len(string)

    if length%2==1:
        print(-1)
        continue
    time=0
    for i in range(0,length//2):
        if string[i]==string[length-1-i]:
            time+=1
    print(time)