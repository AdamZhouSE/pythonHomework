def Test():
    s=input()
    maps=[]
    for i in range(0,127):
        maps.append(0)
    for word in s:
        if(word!=" " and word!="\n"):
            maps[ord(word)]=maps[ord(word)]+1
    sum=0
    for i in range(0,127):
        sum=sum+maps[i]
    print(sum,end="")
if __name__ == "__main__":
    Test()