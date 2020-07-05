def h3():
    s1 = list("CODEFESTIVAL2016")
    s2 = list(input())
    n = len(s1)
    for i in range(n):
        for j in range(n):
            if(s1[i]==s2[j]):
                s1[i] = ""
    sum = 0
    for i in range(n):
        if(s1[i]!=""):
            sum+=1
    print(sum)
if __name__ == '__main__':
    h3()