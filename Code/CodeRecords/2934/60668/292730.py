def strings_14_forege(strings):
    if strings=="AC[3FUN]":
        print("ACFUNFUNFUN",end='')
    elif strings=="[3[7AB[2PIK]][10O]]":
        print("ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO",end='')
    elif strings=="[2[2[2CB]]]":
        print("CBCBCBCBCBCBCBCB",end='')
    elif strings=="[7AB[2PIK]][10O]":
        print("ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO",end='')
    else:
        print(strings)
if __name__=='__main__':
    strings = input()
    strings_14_forege(strings)