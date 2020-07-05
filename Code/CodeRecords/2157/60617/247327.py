def main():
    Rome=input()
    decimal=0
    while len(Rome)>0:
        if Rome[0]=="I":
            if len(Rome)>=2:
                if Rome[1]=="V":
                    decimal+=4
                    Rome=Rome[2:]
                    continue
                elif Rome[1]=="X":
                    decimal+=9
                    Rome=Rome[2:]
                    continue
            decimal+=1
            Rome=Rome[1:]
            continue
        elif Rome[0]=="X":
            if len(Rome)>=2:
                if Rome[1]=="L":
                    decimal+=40
                    Rome=Rome[2:]
                    continue
                elif Rome[1]=="C":
                    decimal+=90
                    Rome=Rome[2:]
                    continue
            decimal+=10
            Rome=Rome[1:]
            continue
        elif Rome[0]=="C":
            if len(Rome)>=2:
                if Rome[1]=="D":
                    decimal+=400
                    Rome=Rome[2:]
                    continue
                elif Rome[1]=="M":
                    decimal+=900
                    Rome=Rome[2:]
                    continue
            decimal+=100
            Rome=Rome[1:]
            continue
        elif Rome[0]=="V":
            decimal+=5
            Rome=Rome[1:]
            continue
        elif Rome[0]=="L":
            decimal+=50
            Rome=Rome[1:]
            continue
        elif Rome[0]=="D":
            decimal+=500
            Rome=Rome[1:]
            continue
        elif Rome[0]=="M":
            decimal+=1000
            Rome=Rome[1:]
            continue
    print(decimal)

if __name__=='__main__':
    main()