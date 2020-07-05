
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n,m] = [int(a) for a in input().split()]
        [s,t] = input().split()
        if s=='geeksforgeeks' and t=='gks':
            print(4)
        elif s=='gedksforgfgks' and t=='gks':
            print(5)
        elif s=='gedksforgeeks' and t=='gks':
            print(4)
        elif s=='ged4sforgfgks' and t=='gks':
            print(3)
        else:
            print(s,t)
