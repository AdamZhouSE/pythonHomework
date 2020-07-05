def DecToRome():
    dec=int(input())
    Rome={"M":1000, "CM":900, "CD":400, "D":500, "C":100, "XC":90, "XL":40,
          "L":50, "X":10, "IX":9, "V":5,
          "IV":4, "I":1}
    result=""
    while dec>0:
        for key in Rome:
            if dec-Rome[key]>=0:
                result+=key
                dec=dec-Rome[key]
            
    print(result)

if __name__=='__main__':
    DecToRome()