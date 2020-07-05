def Test():
    n,m=map(int,input().split())
    words=[]
    for i in range(n):
        words.append(input())
    for i in range(m):
        temp=eval("["+input().replace(" ",",")+"]")
        finds=words[temp[0]-1:temp[1]]
        finds.sort(reverse=True)
        print(finds[0])

if __name__ == "__main__":
    Test()