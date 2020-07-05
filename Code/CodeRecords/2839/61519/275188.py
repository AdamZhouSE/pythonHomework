n=int(input())
list=[]
for i in range(n):
    word=input()
    if word not in list:
        list.append(word)
        print("NO")
    else:
        print("YES")