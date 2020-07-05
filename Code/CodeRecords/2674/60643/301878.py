def  substrings(s):
    count_a=0
    count_b=0
    count_c=0
    for i in s:
        if i=='a':
            count_a=count_a*2+1#每个a可以取代前面的a,或者跟随前一个的a,或者作为新的开始
        elif i=='b':
            count_b=count_b*2+count_a#每个b可以跟随前面的a,或者跟随前一个的b,或者取代前一个的b
        elif i=='c':
            count_c=count_c*2+count_b#每个c可以跟随前面的b,或者跟随前一个的c,或者取代前一个的c
    return count_c


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        ans=substrings(s)
        print(ans)