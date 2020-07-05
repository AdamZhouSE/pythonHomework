def Test():
    aplha=eval(input())
    target=input()
    aplha.sort()
    result=aplha[0]
    for word in aplha:
        if(word>target):
            result=word
            break
    print(result)
if __name__ == "__main__":
    Test()