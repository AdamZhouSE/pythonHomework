a=eval(input())
for i in range(a):
    number=eval(input())
    array=[int(x) for x in input().rstrip().split()]
    def temp():
        for A in range(number):
            for B in range(A+1,number):
                for C in range(A+1,number):
                    if C==B:
                        continue
                    for D in range(C+1,number):
                        if D==B:
                            continue
                        if array[A]+array[B]==array[C]+array[D]:
                            print(A,B,C,D)
                            return "1"
        return "no pairs"
    t=temp()
    if len(t)>0:
        print(t)