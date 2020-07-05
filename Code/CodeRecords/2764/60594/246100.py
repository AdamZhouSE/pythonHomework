n=(int)(input())
for index in range(n):
    xinzonghe=(int)(input())
    now=[]
    now.append(xinzonghe)
    jiuzonghe=0
    while xinzonghe!=jiuzonghe:
        jiuzonghe=xinzonghe
        index=0
        while index<len(now):
            if (int)(now[index]/2)+(int)(now[index]/3)+(int)(now[index]/4)>now[index]:
                xinzonghe = jiuzonghe -now[index]+(int)(now[index]/2)+(int)(now[index]/3)+(int)(now[index]/4)
                now.append((int)(now[index]/2))
                now.append((int)(now[index]/3))
                now.append((int)(now[index]/4))
                now.pop(index)
                break
            index += 1
    print(xinzonghe)