tar=int(input())
guess = 1
while guess*guess < tar:
    if (guess+1)**2 >tar:
        break
    guess +=1
print(guess)