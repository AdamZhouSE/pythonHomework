def Test():
    newspaper="".join(input().split())
    letter="".join(input().split())
    for i in range(0,len(letter)):
        for j in range(0,len(letter)):
            k=letter[i:i+j+1]
            index=newspaper.find(k)
            if(index!=-1):
                newspaper=newspaper[:index]+newspaper[index+len(k):]
                letter=letter[i+j+1:]
                break
    if(letter==""):
        print("YES",end="")
    else:
        print("NO",end="")

if __name__ == "__main__":
    Test()