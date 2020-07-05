n=int(input())
article=''
edit=[]
for ti in range(n):
    act=input()
    if(act[0]=='Q'):
        print(article[int(act[2])-1])
    elif(act[0]=='T'):
        article+=act[2]
    else:
        article=article[:len(article)-int(act[2])]
