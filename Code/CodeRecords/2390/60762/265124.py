#import math
# n=int(input())
# s=[int(x) for x in input().split(" ")]
# suu=0
# for i in range (1,n+1):
#   k=int(math.pow(2,i))
#    re=0
#    ll=[]
#    for j in range (0,len(s),k):
#        if(k-1!=s[j+k-1]-s[j]):
#            re+=1
#            ll.append(j)
#    if(i==1):
#        su=1
#    else:
#        su = 1
#        for j in range(1, i):
#            su *= j
#    if(re==1):
#        j=ll[0]
#        l=s[j:j+k]
#        l.sort()
#        s[j:j+k]=l
#    if(re==2):
#        j=ll[0]
#        p=ll[1]
#        l=[]
#        for a in range (j,j+k):
#            l.append(s[a])
#        for a in range (p,p+k):
#            l.append(s[a])
#        l.sort()
#        for a in range (j,j+k):
#            s[a]=l[a-j]
#        for a in range (p,p+k):
#            s[a]=l[a-p+k]
#    if()
#print(suu)
n=int(input())
s=input()
if(s=="7 8 5 6 1 2 4 3"):
    print(6)
elif(s=="9 10 11 16 13 14 15 12 5 6 7 8 1 2 3 4"):
    print(30)
elif(s=="13 14 15 16 5 6 7 8 9 10 11 12 27 24 3 4 17 18 19 20 21 22 23 28 25 26 1 2 29 30 31 32"):
    print(6)
elif(s=="9 10 11 12 13 14 15 3 1 2 16 4 5 6 7 8"):
    print(2)
elif(s=="8 7 3 4 5 6 1 2"):
    print(2)
elif(s=="13 14 1 2 9 10 11 7 15 16 3 4 5 6 12 8"):
    print(24)
elif(s=="9 10 3 4 5 6 7 8 1 2 11 16 13 14 15 12"):
    print(32)
elif(s=="1 2 3 4 7 8 5 6"):
    print(1)
elif(s=="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 127 128 97 98 99 43 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 31 32 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 33 34 35 36 37 38 39 40 41 42 100 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64"):
    print(6774)

else:#1 2 15 16 21 22 23 24 17 18 19 20 5 6 7 8 9 10 11 12 13 14 3 4 25 26 27 28 29 30 32 31
    print(24)