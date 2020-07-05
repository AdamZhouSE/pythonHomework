def Test():
    height=int(input())
    width=int(input())
    index=int(input())
    map=[]
    line=[]
    for i in range(0,height):
        for j in range(0,width):
            line.append((i+1)*(j+1))
    line.sort()
    print(line[index-1])

if __name__ == "__main__":
    Test()